#!/usr/bin/env python3
"""Convert a paper PDF to a machine-readable Markdown version for LLMs.

Implements the "legible to machines" pattern (Quentin Andre,
https://quentinandre.net/posts/legible-to-machines/): for a paper served at
``/pdfs/papers/<name>.pdf`` we publish a clean Markdown twin at
``/pdfs/papers/<name>.pdf.md`` (his "append .md to the URL" rule). Each .md gets
YAML front matter (title, authors, venue, year, DOI, canonical PDF URL) built
from the canonical metadata in research.qmd, followed by the full converted body.

Engines (best quality first):
  * ``marker``  (default) - datalab-to/marker, purpose-built for scientific PDFs;
                 emits equations as LaTeX, reconstructs tables, multi-column. Add
                 ``--use-llm`` for the LLM verification pass (needs an API key,
                 e.g. GEMINI_API_KEY) - highest fidelity.
  * ``pandoc``  - convert from LaTeX *source* (``--tex path/to/main.tex``) for
                 byte-perfect math on the papers where we have the .tex.

Usage:
  python tools/pdf-to-md.py aer.20181478.pdf            # one paper, marker
  python tools/pdf-to-md.py --all                       # whole corpus, marker
  python tools/pdf-to-md.py --all --cv                  # corpus + CV twin
  python tools/pdf-to-md.py --cv                        # just rebuild the CV twin
  python tools/pdf-to-md.py --all --use-llm             # + LLM refinement pass
  python tools/pdf-to-md.py GTO_Learning_Loss.pdf \
        --engine pandoc --tex "C:/.../maintext.tex"     # from LaTeX source

The CV twin (pdfs/Mauricio-Romero-CV.pdf.md) is built from the LaTeX CV
(default C:\\Users\\mauri\\Dropbox\\CV\\CV-ENG.tex, override with --tex) via
pandoc, which is far cleaner than converting the CV PDF.

Image extraction is disabled: LLMs cannot read figure PNGs and they bloat the
repo. With ``--use-llm`` Marker still writes figure captions/descriptions as text.
The .md files are committed and served as static resources; the GitHub Action
does not run this script.
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paper_metadata import (  # noqa: E402
    PAPERS_DIR,
    REPO_ROOT,
    SITE_URL,
    Paper,
    parse_papers,
)

# The CV is served at /pdfs/Mauricio-Romero-CV.pdf; its machine-readable twin
# follows the same "append .md" rule. Source of truth is the LaTeX CV, which
# converts far cleaner than the PDF (it has the real structure + links).
CV_PDF = REPO_ROOT / "pdfs" / "Mauricio-Romero-CV.pdf"
CV_MD = REPO_ROOT / "pdfs" / "Mauricio-Romero-CV.pdf.md"
CV_TEX_DEFAULT = Path(r"C:\Users\mauri\Dropbox\CV\CV-ENG.tex")
CV_PDF_URL = f"{SITE_URL}/pdfs/Mauricio-Romero-CV.pdf"
CV_MD_URL = f"{SITE_URL}/pdfs/Mauricio-Romero-CV.pdf.md"


def _front_matter(p: Paper) -> str:
    def esc(s: str) -> str:
        return s.replace('"', '\\"').strip()

    lines = ["---", f'title: "{esc(p.title)}"']
    if p.byline:
        lines.append(f'authors_and_venue: "{esc(p.byline)}"')
    if p.venue:
        lines.append(f'venue: "{esc(p.venue)}"')
    if p.year:
        lines.append(f"year: {p.year}")
    if p.doi:
        lines.append(f'doi: "{esc(p.doi)}"')
    if p.abstract:
        lines.append(f'abstract: "{esc(p.abstract)}"')
    lines.append(f'pdf_url: "{p.pdf_url}"')
    lines.append(f'canonical_url: "{p.md_url}"')
    lines.append("source: research.qmd")
    lines.append("note: >-")
    lines.append(
        "  Machine-readable Markdown version of the paper, generated for LLMs."
    )
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def _run(cmd: list[str], env: dict | None = None) -> None:
    # Never echo secrets (e.g. an API key passed via env stays out of stdout).
    print("  $", " ".join(cmd))
    subprocess.run(cmd, check=True, env=env)


def _convert_marker(pdf: Path, out_md: Path, use_llm: bool, thread_cap: int = 0) -> str:
    """Run marker_single into a temp dir and return the produced Markdown body.

    ``thread_cap`` > 0 limits the BLAS/torch thread pools inside the marker
    subprocess, so several conversions can run in parallel (``--jobs``) on a
    multi-core CPU without each grabbing all cores and thrashing.
    """
    exe = shutil.which("marker_single")
    if not exe:
        raise RuntimeError(
            "marker_single not found. Install with: pip install marker-pdf\n"
            "(see requirements-md.txt). Or use --engine pandoc with --tex."
        )
    with tempfile.TemporaryDirectory() as tmp:
        cmd = [
            exe,
            str(pdf),
            "--output_dir",
            tmp,
            "--output_format",
            "markdown",
            "--disable_image_extraction",
        ]
        env = os.environ.copy()
        if thread_cap > 0:
            for var in (
                "OMP_NUM_THREADS",
                "MKL_NUM_THREADS",
                "OPENBLAS_NUM_THREADS",
                "NUMEXPR_NUM_THREADS",
                "TORCH_NUM_THREADS",
            ):
                env[var] = str(thread_cap)
        if use_llm:
            cmd.append("--use_llm")
            # Marker's Gemini service reads GOOGLE_API_KEY; accept either name.
            key = env.get("GOOGLE_API_KEY") or env.get("GEMINI_API_KEY")
            if not key:
                raise RuntimeError(
                    "--use-llm needs GEMINI_API_KEY (or GOOGLE_API_KEY) in the "
                    "environment. Set it inline, e.g. GEMINI_API_KEY=... python ..."
                )
            env["GOOGLE_API_KEY"] = key
            env["GEMINI_API_KEY"] = key
        _run(cmd, env=env)
        produced = sorted(Path(tmp).rglob("*.md"))
        if not produced:
            raise RuntimeError(f"marker produced no .md for {pdf.name}")
        # Largest .md is the manuscript (others may be metadata stubs).
        body = max(produced, key=lambda f: f.stat().st_size).read_text(
            encoding="utf-8"
        )
    return body.strip() + "\n"


def _convert_marker_batch(
    papers: list[Paper], use_llm: bool, workers: int, force: bool
) -> int:
    """Convert many papers in ONE marker process (models load once).

    Marker's folder CLI (``marker IN_FOLDER``) is the right tool for the whole
    corpus: it loads the Surya models a single time and walks the folder, instead
    of paying the multi-minute model-load cost per paper and (worse) spawning
    several model copies at once -- which on Windows exhausts the page file
    (``OSError 1455``). We stage just the target PDFs into a temp input dir,
    run marker over it, then move each result to ``<name>.pdf.md`` with front
    matter prepended.

    Returns the number of .md files written.
    """
    exe = shutil.which("marker")
    if not exe:
        raise RuntimeError(
            "marker (batch CLI) not found. Install with: pip install marker-pdf"
        )
    todo = [
        p
        for p in papers
        if p.pdf_path.exists() and (force or not p.md_path.exists())
    ]
    if not todo:
        print("Nothing to convert (all .md exist; use --force to redo).")
        return 0

    with tempfile.TemporaryDirectory() as tmp:
        in_dir = Path(tmp) / "in"
        out_dir = Path(tmp) / "out"
        in_dir.mkdir()
        out_dir.mkdir()
        # Stage target PDFs (copy; ~51 MB total, trivial).
        for p in todo:
            shutil.copy2(p.pdf_path, in_dir / p.pdf)
        print(f"Batch: {len(todo)} paper(s), {workers} worker(s), models load once.")

        cmd = [
            exe,
            str(in_dir),
            "--output_dir",
            str(out_dir),
            "--output_format",
            "markdown",
            "--disable_image_extraction",
            "--workers",
            str(max(1, workers)),
        ]
        env = os.environ.copy()
        if use_llm:
            cmd.append("--use_llm")
            key = env.get("GOOGLE_API_KEY") or env.get("GEMINI_API_KEY")
            if not key:
                raise RuntimeError(
                    "--use-llm needs GEMINI_API_KEY (or GOOGLE_API_KEY) in env."
                )
            env["GOOGLE_API_KEY"] = key
            env["GEMINI_API_KEY"] = key
        _run(cmd, env=env)

        n = 0
        for p in todo:
            stem = p.pdf[:-4] if p.pdf.lower().endswith(".pdf") else p.pdf
            # marker writes <out>/<stem>/<stem>.md
            cand = list(out_dir.glob(f"{stem}/*.md")) or list(
                out_dir.glob(f"{stem}*/*.md")
            )
            if not cand:
                print(f"   MISSING output for {p.pdf}", file=sys.stderr)
                continue
            body = max(cand, key=lambda f: f.stat().st_size).read_text(
                encoding="utf-8"
            ).strip() + "\n"
            p.md_path.write_text(_front_matter(p) + body, encoding="utf-8")
            kb = p.md_path.stat().st_size / 1024
            print(f"   wrote {p.md_name}  ({kb:.0f} KB)")
            n += 1
    return n


def _convert_pandoc(tex: Path) -> str:
    exe = shutil.which("pandoc")
    if not exe:
        raise RuntimeError("pandoc not found on PATH.")
    out = subprocess.run(
        [
            exe,
            str(tex),
            "--from",
            "latex",
            "--to",
            "gfm",
            "--wrap",
            "none",
            "--markdown-headings",
            "atx",
        ],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return out.stdout.strip() + "\n"


def _clean_cv_markdown(md: str) -> str:
    """Strip pandoc/LaTeX artifacts from the converted CV.

    The CV LaTeX uses ``\\begin{center}`` (-> ``<div class="center">``), a
    pstricks ``\\put`` rule that surfaces as a stray ``(1,0)500`` line, hard
    line-breaks (trailing ``\\``), and a few ``$`...`$`` math escapes around
    plain ``|`` / superscripts. None of that helps an LLM; flatten to clean prose.
    """
    import re

    out = []
    for line in md.splitlines():
        s = line.rstrip()
        st = s.strip()
        if st in ('<div class="center">', "</div>"):
            continue
        if st == "(1,0)500":  # pstricks rule artifact
            continue
        if st == "\\":  # lone hard-break line
            continue
        s = s.rstrip("\\").rstrip()          # drop trailing hard-breaks
        s = s.replace("$`|`$", "|")          # G^2LM|LIC, Quantil | etc.
        s = re.sub(r"\$`\^?\{?([^`}]*)\}?`\$", r"\1", s)  # $`^2`$ -> 2
        out.append(s)

    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)   # collapse blank runs
    return text.strip() + "\n"


def _cv_front_matter() -> str:
    return (
        "---\n"
        'title: "Curriculum Vitae — Mauricio Romero"\n'
        'description: "Full academic CV of Mauricio Romero (ITAM): positions, '
        "education, publications, working papers, grants, awards, teaching, and "
        'service."\n'
        'source: "CV-ENG.tex"\n'
        f'pdf_url: "{CV_PDF_URL}"\n'
        f'canonical_url: "{CV_MD_URL}"\n'
        "note: >-\n"
        "  Machine-readable Markdown version of the CV, generated for LLMs from "
        "the canonical LaTeX source.\n"
        "---\n\n"
    )


def convert_cv(tex: Path | None, force: bool) -> bool:
    """Build pdfs/Mauricio-Romero-CV.pdf.md from the LaTeX CV via pandoc."""
    src = tex or CV_TEX_DEFAULT
    if not src.exists():
        raise RuntimeError(f"CV LaTeX source not found: {src}")
    if CV_MD.exists() and not force:
        print(f"SKIP  {CV_MD.name} (exists; use --force to overwrite)")
        return False

    print(f"CONVERT CV  {src.name}  ->  {CV_MD.name}  [pandoc]")
    # pandoc wants a UTF-8 file; the CV is latin1/ascii -> normalize via temp.
    raw = src.read_bytes()
    for enc in ("utf-8", "latin-1", "cp1252"):
        try:
            txt = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    else:
        raise RuntimeError(f"could not decode {src}")

    with tempfile.TemporaryDirectory() as tmp:
        norm = Path(tmp) / "cv.tex"
        norm.write_text(txt, encoding="utf-8")
        body = _clean_cv_markdown(_convert_pandoc(norm))

    CV_MD.write_text(_cv_front_matter() + body, encoding="utf-8")
    kb = CV_MD.stat().st_size / 1024
    print(f"   wrote {CV_MD}  ({kb:.0f} KB)")
    return True


def convert_one(
    paper: Paper,
    engine: str,
    use_llm: bool,
    tex: Path | None,
    force: bool,
    thread_cap: int = 0,
) -> bool:
    if paper.md_path.exists() and not force:
        print(f"SKIP  {paper.md_name} (exists; use --force to overwrite)")
        return False
    if not paper.pdf_path.exists() and engine != "pandoc":
        print(f"SKIP  {paper.pdf} (PDF missing)")
        return False

    print(f"CONVERT {paper.pdf}  ->  {paper.md_name}  [{engine}]")
    if engine == "pandoc":
        if tex is None or not tex.exists():
            raise RuntimeError("--engine pandoc requires --tex PATH to a .tex file")
        body = _convert_pandoc(tex)
    else:
        body = _convert_marker(paper.pdf_path, paper.md_path, use_llm, thread_cap)

    paper.md_path.write_text(_front_matter(paper) + body, encoding="utf-8")
    kb = paper.md_path.stat().st_size / 1024
    print(f"   wrote {paper.md_path}  ({kb:.0f} KB)")
    return True


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("pdf", nargs="?", help="PDF basename in pdfs/papers/, or omit with --all")
    ap.add_argument("--all", action="store_true", help="convert every paper in research.qmd")
    ap.add_argument(
        "--cv",
        action="store_true",
        help="(also) build the CV twin pdfs/Mauricio-Romero-CV.pdf.md from the "
        "LaTeX source (pandoc). Combine with --all, or use alone.",
    )
    ap.add_argument("--engine", choices=["marker", "pandoc"], default="marker")
    ap.add_argument("--use-llm", action="store_true", help="marker LLM refinement pass")
    ap.add_argument("--tex", type=Path, help="LaTeX source (for --engine pandoc)")
    ap.add_argument("--force", action="store_true", help="overwrite existing .md")
    ap.add_argument(
        "--jobs",
        type=int,
        default=1,
        help="marker batch worker count for multi-paper runs (one process, "
        "models loaded once). Keep modest (2-4) to stay within the page file. "
        "Default 1 (safest).",
    )
    args = ap.parse_args(argv)

    papers = parse_papers()
    by_pdf = {p.pdf: p for p in papers}

    # --cv may run alone (no paper targets) or alongside --all / a single paper.
    cv_only = args.cv and not args.all and not args.pdf
    if args.all:
        targets = papers
    elif args.pdf:
        key = args.pdf
        if key not in by_pdf:
            # allow passing the .pdf.md or a path
            key = Path(key).name.removesuffix(".md")
        if key not in by_pdf:
            print(f"error: '{args.pdf}' is not a paper in research.qmd", file=sys.stderr)
            print("known:", ", ".join(sorted(by_pdf)), file=sys.stderr)
            return 2
        targets = [by_pdf[key]]
    elif args.cv:
        targets = []
    else:
        ap.print_help()
        return 2

    PAPERS_DIR.mkdir(parents=True, exist_ok=True)
    jobs = max(1, args.jobs)

    # Convert the CV first if requested (fast pandoc step).
    if args.cv:
        try:
            convert_cv(args.tex, args.force)
        except Exception as e:
            print(f"   FAILED CV: {e}", file=sys.stderr)
        if cv_only:
            print("\nDone (CV). Now run: python tools/gen-llms-txt.py")
            return 0

    # Whole-corpus marker runs use batch mode: ONE process, models loaded once,
    # walks the folder. This avoids both the per-paper model-reload cost and the
    # page-file exhaustion (OSError 1455) seen when several marker_single
    # processes load the models concurrently. --jobs sets marker's worker count
    # inside that single process.
    if args.engine == "marker" and len(targets) > 1:
        n = _convert_marker_batch(targets, args.use_llm, jobs, args.force)
        print(f"\nDone. {n} file(s) written. Now run: python tools/gen-llms-txt.py")
        return 0

    def _do(p: Paper) -> bool:
        try:
            return convert_one(
                p, args.engine, args.use_llm, args.tex, args.force, 0
            )
        except Exception as e:  # keep going across the corpus
            print(f"   FAILED {p.pdf}: {e}", file=sys.stderr)
            return False

    n = sum(1 for p in targets if _do(p))
    print(f"\nDone. {n} file(s) written. Now run: python tools/gen-llms-txt.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
