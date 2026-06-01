#!/usr/bin/env python3
"""Insert a `· [Markdown](/pdfs/papers/<name>.pdf.md)` link into each research.qmd
entry whose machine-readable twin already exists.

Idempotent and self-healing: skips entries that already have the link, and only
adds links for papers whose ``.pdf.md`` is on disk (so it never creates a dead
link / trips the link-check hook). Re-run it after `pdf-to-md.py --all` finishes
to pick up newly converted papers.

For a normal entry it appends the link to the existing link row (the line that
starts with a ``[Label](...)`` and is dot-separated, e.g.
``[Final Manuscript](...) · [Data and code](...)``). For entries that have no
link row (some resting papers whose title is the PDF link), it inserts a fresh
one-link row right after the paper-head's closing ``:::``.

Usage:  python tools/add-md-links.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paper_metadata import RESEARCH_QMD, parse_papers  # noqa: E402

LINK_ROW_RE = re.compile(r"^\[[^\]]+\]\((?:/pdfs/|https?:)")


def _entry_span(text: str, pdf: str):
    """Return (start, end) char offsets of the entry that references `pdf`.

    An entry runs from a `::: {.paper-head}` marker to the next paper-head or the
    next `## ` section heading. We match the entry whose body contains the pdf.
    """
    # Boundaries: paper-head markers and section headings.
    bounds = [m.start() for m in re.finditer(r"^:::\s*\{\.paper-head\}\s*$", text, re.M)]
    bounds += [m.start() for m in re.finditer(r"^##\s+", text, re.M)]
    bounds = sorted(set(bounds)) + [len(text)]
    heads = [m.start() for m in re.finditer(r"^:::\s*\{\.paper-head\}\s*$", text, re.M)]
    enc = re.escape(pdf).replace(r"\ ", r"(?:\ |%20)")
    needle = re.compile(rf"/pdfs/papers/{enc}\b")
    for h in heads:
        nxt = min((b for b in bounds if b > h), default=len(text))
        if needle.search(text[h:nxt]):
            return h, nxt
    return None


def process(dry_run: bool = False) -> int:
    text = RESEARCH_QMD.read_text(encoding="utf-8")
    papers = [p for p in parse_papers() if p.md_path.exists()]
    added = 0
    # Work back-to-front so offsets stay valid as we splice.
    spans = []
    for p in papers:
        span = _entry_span(text, p.pdf)
        if span:
            spans.append((span[0], span[1], p))
    spans.sort(key=lambda s: s[0], reverse=True)

    for start, end, p in spans:
        entry = text[start:end]
        md_link = f"[Markdown](/pdfs/papers/{p.md_name.replace(' ', '%20')})"
        if "[Markdown](" in entry:
            continue  # already linked
        lines = entry.splitlines()
        # Find an existing link row.
        row_idx = None
        for i, ln in enumerate(lines):
            if LINK_ROW_RE.match(ln.strip()):
                row_idx = i
                break
        if row_idx is not None:
            lines[row_idx] = lines[row_idx].rstrip() + f" · {md_link}"
        else:
            # Insert a fresh link row after the paper-head close (first `:::`
            # that closes the head), else right after the title.
            close_idx = None
            seen_head = False
            for i, ln in enumerate(lines):
                if ln.strip().startswith("::: {.paper-head}"):
                    seen_head = True
                elif seen_head and ln.strip() == ":::":
                    close_idx = i
                    break
            insert_at = (close_idx + 1) if close_idx is not None else 1
            lines.insert(insert_at, "")
            lines.insert(insert_at + 1, md_link)
        text = text[:start] + "\n".join(lines) + ("\n" if entry.endswith("\n") else "") + text[end:]
        added += 1

    if not dry_run and added:
        RESEARCH_QMD.write_text(text, encoding="utf-8")
    print(f"{'(dry-run) ' if dry_run else ''}Added {added} Markdown link(s) "
          f"for {len(papers)} paper(s) with a .pdf.md.")
    return 0


if __name__ == "__main__":
    sys.exit(process(dry_run="--dry-run" in sys.argv))
