#!/usr/bin/env python3
"""Generate the root ``llms.txt`` index from research.qmd.

Follows the llms.txt convention (https://llmstxt.org/) and Quentin Andre's
"legible to machines" guidance: an H1 name, a blockquote summary, then
Markdown link lists grouped by site section. Each paper points at its
machine-readable ``.pdf.md`` twin, with the original PDF noted alongside.

Only papers that already have a generated ``<name>.pdf.md`` are listed, so the
index never advertises a file that 404s (and never trips the link-check hook).
Run after ``pdf-to-md.py``:

    python tools/gen-llms-txt.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paper_metadata import REPO_ROOT, SITE_URL, parse_papers  # noqa: E402

LLMS_TXT = REPO_ROOT / "llms.txt"
CV_MD = REPO_ROOT / "pdfs" / "Mauricio-Romero-CV.pdf.md"
CV_MD_URL = f"{SITE_URL}/pdfs/Mauricio-Romero-CV.pdf.md"
CV_PDF_URL = f"{SITE_URL}/pdfs/Mauricio-Romero-CV.pdf"

HEADER = f"""# Mauricio Romero

> Associate Professor of Economics at ITAM (Mexico City) and Co-Editor of the
> Journal of Development Economics. Research in development, education, public,
> and environmental economics using applied microeconometrics and randomized
> controlled trials. This file indexes machine-readable Markdown versions of his
> papers for language models. Each link points to a clean Markdown rendering of
> the paper; the original PDF is noted in parentheses. Site: {SITE_URL}
"""

# Order sections the way they appear on the Research page.
SECTION_ORDER = [
    "Publications (peer-reviewed)",
    "Comments, conference proceedings, and others",
    "Non-economics peer-reviewed articles",
    "Working papers",
    "Resting papers",
]


def _section_key(section: str) -> tuple[int, str]:
    try:
        return (SECTION_ORDER.index(section), "")
    except ValueError:
        return (len(SECTION_ORDER), section)


def main(argv=None) -> int:
    papers = [p for p in parse_papers() if p.md_path.exists()]
    if not papers and not CV_MD.exists():
        print(
            "No .pdf.md files found yet. Run pdf-to-md.py first; nothing written.",
            file=sys.stderr,
        )
        return 1

    papers.sort(key=lambda p: (_section_key(p.section), -int(p.year or 0)))

    out = [HEADER]
    if CV_MD.exists():
        out.append("\n## Curriculum Vitae\n")
        out.append(
            f"- [Curriculum Vitae — Mauricio Romero]({CV_MD_URL}): full CV "
            f"(positions, education, publications, grants, awards, teaching, "
            f"service). (PDF: {CV_PDF_URL})"
        )
    current = None
    for p in papers:
        if p.section != current:
            current = p.section
            out.append(f"\n## {current or 'Papers'}\n")
        desc = p.one_line()
        line = f"- [{p.title}]({p.md_url})"
        if desc and desc != p.title:
            line += f": {desc}"
        line += f" (PDF: {p.pdf_url})"
        out.append(line)

    out.append("")  # trailing newline
    LLMS_TXT.write_text("\n".join(out), encoding="utf-8")
    cv = " + CV" if CV_MD.exists() else ""
    print(f"Wrote {LLMS_TXT} ({len(papers)} papers{cv}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
