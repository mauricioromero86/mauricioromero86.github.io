#!/usr/bin/env python3
"""Backfill Markdown twins for the NON-primary PDFs in ``pdfs/papers/``.

``pdf-to-md.py --all`` only converts the primary manuscript of each paper in
``research.qmd``; appendices, journal supplements, and superseded drafts are
skipped. This helper converts everything else in the folder so that *any*
``/pdfs/papers/<name>.pdf`` URL also serves ``<name>.pdf.md`` (the append-`.md`
convention). These twins are deliberately NOT indexed in ``llms.txt`` and get
no on-page ``[Markdown]`` link — they exist only for agents that follow an
appendix/draft URL directly.

Front matter marks what each file is: appendices/supplements point to the
paper they accompany; superseded drafts carry an explicit warning naming the
published version (machine-readable copies of outdated results must say so).
The parent paper is derived from ``research.qmd`` itself (``extra_pdfs`` of
``parse_papers()``), not guessed.

Usage:
  python tools/convert-appendix-md.py            # convert all missing twins
  python tools/convert-appendix-md.py --jobs 2   # marker batch workers (keep <=2-3)
  python tools/convert-appendix-md.py --force    # redo existing twins too

One ``marker`` batch process (models load once); CPU-only box => hours.
Run in the background. Never spawn parallel marker_single processes.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paper_metadata import PAPERS_DIR, SITE_URL, parse_papers  # noqa: E402

# Files that are genuine appendices/supplements to a current paper. Everything
# else without a twin is a superseded draft / auxiliary copy and gets the
# stale-results warning instead.
APPENDIX_FILES = {
    "Appendix_crosscuts.pdf",
    "CG_Preference_Tables.pdf",
    "1-s2.0-S0272775723001395-mmc1.pdf",
    "TN_ECE_VA.pdf",
}

# Parent papers for files no longer linked from research.qmd. Verified by
# filename/title correspondence; the mmc1 supplement's PII resolves to the
# GTO paper's DOI via Crossref (10.1016/j.econedurev.2023.102492).
PARENT_HINTS = {
    "1-s2.0-S0272775723001395-mmc1.pdf": "GTO_Learning_Loss.pdf",
    "Manuscript_TNLL.pdf": "Forthcoming_JHR_TNLL.pdf",
    "PSL_Final.pdf": "PSL_Endline_Short.pdf",
    "Forthcoming_Economica_Grants.pdf": "Grants_Test_Scores_Mexico.pdf",
    "Factorial Designs (Current WP).pdf": "rest_a_01317.pdf",
    "Communal Property Rights and Deforestation.pdf": "RomeroSaavedra_CommunalLands.pdf",
    "Paper_royalties_illegal.pdf": "1-s2.0-S0014292121001768-main.pdf",
}


def _title_from_name(name: str) -> str:
    stem = name[:-4] if name.lower().endswith(".pdf") else name
    return stem.replace("_", " ").strip()


def _front_matter(pdf_name: str, parent) -> str:
    def esc(s: str) -> str:
        return s.replace('"', '\\"').strip()

    pdf_url = f"{SITE_URL}/pdfs/papers/{quote(pdf_name)}"
    md_url = f"{SITE_URL}/pdfs/papers/{quote(pdf_name + '.md')}"

    if pdf_name in APPENDIX_FILES:
        kind = "appendix"
        if parent:
            note = (
                f"Online appendix/supplement to \\\"{esc(parent.title)}\\\" "
                f"({parent.pdf_url}). Generated for LLMs."
            )
        else:
            note = "Online appendix/supplement. Generated for LLMs."
    else:
        kind = "superseded-draft"
        if parent:
            note = (
                f"SUPERSEDED DRAFT - an old version of \\\"{esc(parent.title)}\\\". "
                f"The current version is {parent.pdf_url}; cite and rely on that "
                "version, not this one. Generated for LLMs."
            )
        else:
            note = (
                "SUPERSEDED DRAFT - an old working-paper version kept only so "
                "existing links resolve. A newer published version exists; see "
                f"{SITE_URL}/research.html. Generated for LLMs."
            )

    lines = [
        "---",
        f'title: "{esc(_title_from_name(pdf_name))}"',
        f'document_type: "{kind}"',
    ]
    if parent:
        lines.append(f'parent_paper: "{esc(parent.title)}"')
        lines.append(f'parent_pdf_url: "{parent.pdf_url}"')
    lines += [
        f'pdf_url: "{pdf_url}"',
        f'canonical_url: "{md_url}"',
        "source: pdfs/papers (non-primary document)",
        f'note: "{note}"',
        "---",
    ]
    return "\n".join(lines) + "\n\n"


def collect_targets(force: bool):
    """(pdf_path, parent Paper|None) for every non-primary PDF lacking a twin."""
    papers = parse_papers()
    primaries = {p.pdf for p in papers}
    by_pdf = {p.pdf: p for p in papers}
    parent_of = {
        extra: by_pdf[primary]
        for extra, primary in PARENT_HINTS.items()
        if primary in by_pdf
    }
    for p in papers:
        for extra in p.extra_pdfs:
            parent_of.setdefault(extra, p)

    todo = []
    for pdf in sorted(PAPERS_DIR.glob("*.pdf")):
        if pdf.name in primaries:
            continue  # pdf-to-md.py territory
        md = PAPERS_DIR / (pdf.name + ".md")
        if md.exists() and not force:
            continue
        todo.append((pdf, parent_of.get(pdf.name)))
    return todo


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--jobs", type=int, default=2, help="marker batch workers (<=2-3)")
    ap.add_argument("--force", action="store_true", help="overwrite existing .md")
    args = ap.parse_args(argv)

    exe = shutil.which("marker")
    if not exe:
        raise RuntimeError("marker (batch CLI) not found: pip install marker-pdf")

    todo = collect_targets(args.force)
    if not todo:
        print("Nothing to convert (all non-primary twins exist; --force to redo).")
        return 0
    for pdf, parent in todo:
        tag = "appendix " if pdf.name in APPENDIX_FILES else "superseded"
        print(f"  [{tag}] {pdf.name}  (parent: {parent.pdf if parent else '-'})")

    with tempfile.TemporaryDirectory() as tmp:
        in_dir = Path(tmp) / "in"
        out_dir = Path(tmp) / "out"
        in_dir.mkdir()
        out_dir.mkdir()
        for pdf, _ in todo:
            shutil.copy2(pdf, in_dir / pdf.name)

        print(f"Batch: {len(todo)} file(s), {args.jobs} worker(s), models load once.")
        cmd = [
            exe,
            str(in_dir),
            "--output_dir",
            str(out_dir),
            "--output_format",
            "markdown",
            "--disable_image_extraction",
            "--workers",
            str(max(1, args.jobs)),
        ]
        print("  $", " ".join(cmd))
        subprocess.run(cmd, check=True)

        n = 0
        for pdf, parent in todo:
            stem = pdf.name[:-4]
            cand = [
                f
                for d in out_dir.iterdir()
                if d.is_dir() and d.name.startswith(stem)
                for f in d.glob("*.md")
            ]
            if not cand:
                print(f"   MISSING output for {pdf.name}", file=sys.stderr)
                continue
            body = max(cand, key=lambda f: f.stat().st_size).read_text(
                encoding="utf-8"
            ).strip() + "\n"
            out_md = PAPERS_DIR / (pdf.name + ".md")
            out_md.write_text(_front_matter(pdf.name, parent) + body, encoding="utf-8")
            print(f"   wrote {out_md.name}  ({out_md.stat().st_size / 1024:.0f} KB)")
            n += 1

    print(f"\nDone. {n} of {len(todo)} twin(s) written.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
