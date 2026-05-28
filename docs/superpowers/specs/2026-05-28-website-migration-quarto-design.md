# Website Migration: WordPress (Bluehost) → Quarto on GitHub Pages

**Date:** 2026-05-28
**Owner:** Mauricio Romero
**Status:** Design — awaiting approval

## Goal

Replace the WordPress/Mesmerize site at `mauricio-romero.com` (Bluehost) with a
static Quarto site hosted on GitHub Pages. Outcome: all content editable as plain
Markdown in a git repo, no database, no server, free hosting, and Bluehost
eventually dropped.

## Why this approach

- **Quarto** matches the owner's existing R/Stata academic toolchain, runs cleanly
  on Windows via a single installer, and uses Markdown content — exactly the
  hand-edited, per-entry publication workflow requested.
- **GitHub Pages** is free, git-native, and integrates with a GitHub Action so a
  push auto-builds and deploys (Quarto local needed only for `quarto preview`).
- Alternatives rejected: **al-folio (Jekyll)** — gold-standard look but its
  signature feature is `.bib`-driven publications (not wanted) and it needs a
  Ruby/Jekyll toolchain that is painful on Windows. **Hugo** — least friendly
  templating, fragmented academic theme ecosystem post-Wowchemy.

## Decisions (locked)

| Topic | Decision |
|-------|----------|
| Framework | Quarto |
| Host | GitHub Pages |
| Publications | Hand-written per-entry Markdown blocks (no `.bib` pipeline) |
| Design | Clean academic Bootswatch theme (default `litera` or `cosmo`) + light `styles.scss` |
| PDFs | All PDFs in-repo, Ghostscript-compressed to fit under ~1 GB; prune oldest course-years if still over |
| Contact | Email + Scholar/Twitter/Bluesky links; no form |
| Domain cutover | Launch on `*.github.io` first → verify → point DNS to Pages. Add redirect on old Bluehost site during transition until host/domain lapses |

## Site structure

Mirrors the current four sections: Bio/CV (home), Research, Data & Code, Teaching.

```
mauricio-romero.com/            (new git repo, repo root)
├── _quarto.yml                 # site config: theme, navbar, output dir
├── index.qmd                   # Bio/CV homepage
├── research.qmd                # Publications (hand-written entries)
├── data-code.qmd               # Data & Code
├── teaching.qmd                # Teaching (links to course PDFs)
├── styles.scss                 # accent color, fonts
├── CNAME                       # custom domain (added at cutover)
├── pdfs/                       # papers, CV, teaching notes (compressed)
├── img/                        # profile photo + images
└── .github/workflows/publish.yml
```

The existing `public_html/` WordPress download remains on disk as source material
but is excluded from the site repo (`.gitignore`), not deleted.

## Content model

Each page is a `.qmd` Markdown file. A publication is a repeatable block the owner
copies and edits — no central index, no build step beyond Quarto's render:

```markdown
### Paper Title
*with Coauthor A, Coauthor B* · *Journal*, Year (or "Forthcoming")

[PDF](pdfs/papers/file.pdf) · [Journal](https://doi.org/...) · [BibTeX](#bibtex-key)

> Abstract text (optional, collapsible via callout).
```

Adding a paper = paste a block + drop the PDF in `pdfs/papers/`.

## PDF handling

- Source: `public_html/pdfs/` = 2.3 GB, 733 PDFs. Largest are 20–37 MB image-heavy
  lecture notes.
- Plan: batch-compress with Ghostscript `-dPDFSETTINGS=/ebook` (expect 3–10×
  reduction on scan/figure-heavy files). Report before/after total size.
- Target: site under ~1 GB (GitHub Pages soft recommendation). If still over after
  compression, prune oldest course-years (owner approves the prune list).
- Hard constraints respected: no single file > 100 MB (current max 37 MB, fine).

## Deployment

- GitHub Action (`quarto-dev/quarto-actions`) builds on push to `main`, publishes
  rendered `_site/` to `gh-pages` branch; Pages serves `gh-pages`.
- Phase 1: site live at `https://<username>.github.io/...` for verification.
- Phase 2 (cutover): add `CNAME` = `mauricio-romero.com`, update Bluehost DNS
  A/CNAME records to GitHub Pages IPs, enable HTTPS in repo Pages settings.
- Transition: place a redirect (`<meta http-equiv="refresh">` / `.htaccess`) on the
  old Bluehost `public_html` pointing to the new site, active until host lapses.

## Migration procedure (high level)

1. Install Quarto (`winget install --id Posit.Quarto -e`).
2. Init git repo at project root; create GitHub repo via `gh`.
3. Scaffold Quarto site (`_quarto.yml`, 4 `.qmd` pages, theme).
4. Extract current page text from the live site → convert to Markdown → owner
   reviews/corrects.
5. Compress PDFs; copy into `pdfs/`; fix internal links.
6. Add GitHub Action; deploy to `*.github.io`; verify all pages + PDF links.
7. Cutover: CNAME + DNS; verify HTTPS; add redirect on old site.
8. Decommission Bluehost once domain resolves to Pages and is verified.

## Tooling status

| Tool | Status |
|------|--------|
| git 2.53 | installed |
| winget | available |
| gh CLI 2.88 | installed |
| Quarto | NOT installed — single `winget` install |
| R / Python / LaTeX | not required (content-only site) |

## Out of scope

- `.bib`-driven automated publication lists.
- Blog/news feed (not present on current site).
- Contact form processing.
- Migrating WordPress core, plugins, or the MySQL database.

## Verification criteria

- All four pages render and match the current site's content.
- Every PDF link resolves (script-checked against the file list).
- Site total under ~1 GB.
- Site live and HTTPS-valid on the custom domain.
- Old site redirects to the new one during transition.
