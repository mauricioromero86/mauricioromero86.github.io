#!/usr/bin/env python3
"""Parse research.qmd into structured per-paper metadata.

Single source of truth for the machine-readable-paper pipeline. Both
``pdf-to-md.py`` (front-matter generation) and ``gen-llms-txt.py`` (the root
``llms.txt`` index) import :func:`parse_papers` from here so the two never drift.

The site lists publications as hand-written Markdown blocks (no .bib pipeline).
Each block looks like::

    ::: {.paper-head}
    ### 1. [Title](journal-url)
    [Abstract](#abs-1){...} [BibTeX](#bib-1){...}
    :::

    with Coauthor A and Coauthor B · **Venue** 134(3), 2019

    [Final Manuscript](/pdfs/papers/file.pdf) · [Data and code](...) · ...

    ::: {#abs-1 .collapse .paper-panel}
    Abstract text...
    :::

    ::: {#bib-1 .collapse .paper-panel}
    ```bibtex
    @article{key, ..., doi={10.x/y} }
    ```
    :::

We extract, per entry that has at least one local ``/pdfs/papers/*.pdf`` link:
title, byline (coauthors + venue + year), the primary manuscript PDF basename,
DOI (from the BibTeX block), abstract, and the on-site section heading.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import quote

REPO_ROOT = Path(__file__).resolve().parent.parent
RESEARCH_QMD = REPO_ROOT / "research.qmd"
PAPERS_DIR = REPO_ROOT / "pdfs" / "papers"
SITE_URL = "https://mauricio-romero.com"

# Link labels that mark the *main* manuscript, in priority order. The first one
# present in an entry's link row wins; otherwise we fall back to the title link
# or the first local PDF found. The published version is preferred when present
# (it is the canonical text); accepted/working manuscripts come next.
PRIMARY_LABEL_PRIORITY = (
    "Published version",
    "Final Manuscript",
    "Working Paper",
    "Manuscript",
)

PDF_LINK_RE = re.compile(r"\[([^\]]+)\]\(/pdfs/papers/([^)]+?\.pdf)\)")
TITLE_RE = re.compile(r"^###\s+(?:\d+\.\s+)?(.*)$", re.MULTILINE)
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
DOI_RE = re.compile(r"doi\s*=\s*\{([^}]+)\}", re.IGNORECASE)
YEAR_RE = re.compile(r"\b(19|20)\d{2}\b")
VENUE_RE = re.compile(r"\*\*(.+?)\*\*")


def _decode_pdf_path(encoded: str) -> str:
    """`Communal%20Property...pdf` -> real on-disk filename with spaces."""
    from urllib.parse import unquote

    return unquote(encoded)


def _strip_md(text: str) -> str:
    """Flatten inline Markdown links/emphasis to plain text for bylines/titles."""
    text = MD_LINK_RE.sub(r"\1", text)
    text = text.replace("**", "").replace("*", "").replace("·", "-")
    return re.sub(r"\s+", " ", text).strip()


@dataclass
class Paper:
    title: str
    pdf: str                      # on-disk basename, e.g. "aer.20181478.pdf"
    section: str                  # site section heading the entry sits under
    byline: str = ""             # coauthors + venue + year, plain text
    venue: str = ""
    year: str = ""
    doi: str = ""
    abstract: str = ""
    extra_pdfs: list[str] = field(default_factory=list)  # appendices, etc.

    @property
    def pdf_url(self) -> str:
        return f"{SITE_URL}/pdfs/papers/{quote(self.pdf)}"

    @property
    def md_name(self) -> str:
        # Andre's convention: append `.md` to the document URL.
        return f"{self.pdf}.md"

    @property
    def md_url(self) -> str:
        return f"{SITE_URL}/pdfs/papers/{quote(self.md_name)}"

    @property
    def md_path(self) -> Path:
        return PAPERS_DIR / self.md_name

    @property
    def pdf_path(self) -> Path:
        return PAPERS_DIR / self.pdf

    def one_line(self) -> str:
        """One-line description for the llms.txt index."""
        bits = [b for b in (self.byline,) if b]
        return " ".join(bits) if bits else self.title


def _split_entries(text: str):
    """Yield (section_heading, entry_text) for each `.paper-head` block.

    entry_text runs from the paper-head marker up to the next paper-head marker
    or the next `## ` section heading, whichever comes first.
    """
    section = ""
    # Tokenize on section headings and paper-head markers while keeping offsets.
    markers = []
    for m in re.finditer(r"^##\s+(.*)$", text, re.MULTILINE):
        markers.append((m.start(), "section", m.group(1).strip()))
    for m in re.finditer(r"^:::\s*\{\.paper-head\}\s*$", text, re.MULTILINE):
        markers.append((m.start(), "head", None))
    markers.sort(key=lambda t: t[0])

    for i, (pos, kind, val) in enumerate(markers):
        if kind == "section":
            section = val
            continue
        end = markers[i + 1][0] if i + 1 < len(markers) else len(text)
        yield section, text[pos:end]


def _extract_abstract(entry: str) -> str:
    m = re.search(
        r":::\s*\{#abs-\d+[^}]*\}\s*(.*?)\n:::", entry, re.DOTALL
    )
    if not m:
        return ""
    return re.sub(r"\s+", " ", m.group(1)).strip()


def _extract_byline_venue_year(entry: str):
    """Return (byline, venue, year) from the first prose line after the head."""
    # The byline is the first non-empty, non-div, non-link-row paragraph after
    # the closing `:::` of the paper-head.
    after_head = entry.split(":::", 2)
    body = after_head[2] if len(after_head) >= 3 else entry
    for raw in body.splitlines():
        line = raw.strip()
        if not line or line.startswith(":::") or line.startswith("```"):
            continue
        if line.startswith("[") and "](" in line and "·" in line:
            # This is the links row (starts with a link, dot-separated); skip.
            # The byline may also contain links but also venue text; we detect
            # the byline by presence of a **Venue** or the word "Forthcoming"
            # or "with ".
            if "**" not in line and "Forthcoming" not in line:
                continue
        if line.startswith("[") and "](" in line and "·" not in line and "**" not in line:
            continue
        byline = _strip_md(line)
        venue_m = VENUE_RE.search(line)
        venue = venue_m.group(1).strip() if venue_m else ""
        year_m = YEAR_RE.search(line)
        year = year_m.group(0) if year_m else ""
        return byline, venue, year
    return "", "", ""


def parse_papers(qmd_path: Path = RESEARCH_QMD) -> list[Paper]:
    text = qmd_path.read_text(encoding="utf-8")
    papers: list[Paper] = []

    for section, entry in _split_entries(text):
        # Title (first ### line in the entry).
        tm = TITLE_RE.search(entry)
        if not tm:
            continue
        title = _strip_md(tm.group(1))

        # All local PDFs referenced in the entry.
        found = [
            (label, _decode_pdf_path(path))
            for label, path in PDF_LINK_RE.findall(entry)
        ]
        if not found:
            continue  # entry has no local manuscript -> nothing to convert

        # Pick the primary manuscript.
        primary = None
        for want in PRIMARY_LABEL_PRIORITY:
            for label, pdf in found:
                if label.strip().lower() == want.lower():
                    primary = pdf
                    break
            if primary:
                break
        if primary is None:
            # title link to a pdf?
            tline = tm.group(1)
            tlink = MD_LINK_RE.search(tline)
            if tlink and "/pdfs/papers/" in tlink.group(2):
                primary = _decode_pdf_path(tlink.group(2).split("/pdfs/papers/")[1])
            else:
                primary = found[0][1]

        extra = [pdf for _, pdf in found if pdf != primary]
        byline, venue, year = _extract_byline_venue_year(entry)
        doi_m = DOI_RE.search(entry)
        doi = doi_m.group(1).strip() if doi_m else ""
        abstract = _extract_abstract(entry)

        papers.append(
            Paper(
                title=title,
                pdf=primary,
                section=section,
                byline=byline,
                venue=venue,
                year=year,
                doi=doi,
                abstract=abstract,
                extra_pdfs=extra,
            )
        )
    return papers


def main(argv=None) -> int:
    """`python tools/paper_metadata.py` prints a summary for sanity-checking."""
    papers = parse_papers()
    missing = []
    for p in papers:
        flag = "" if p.pdf_path.exists() else "  [PDF MISSING]"
        has_md = "md" if p.md_path.exists() else "--"
        print(f"[{has_md}] {p.pdf:<45} {p.year:>4}  doi={p.doi or '-'}{flag}")
        if not p.pdf_path.exists():
            missing.append(p.pdf)
    print(f"\n{len(papers)} papers parsed; {len(missing)} with missing PDFs.")
    if missing:
        print("Missing:", ", ".join(missing))
    return 0


if __name__ == "__main__":
    sys.exit(main())
