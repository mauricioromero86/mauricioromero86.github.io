# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

Migration of Mauricio Romero's academic website from **WordPress/Mesmerize on Bluehost**
(`https://mauricio-romero.com`) to a **static Quarto site on GitHub Pages**. The goal is an
academic site that is editable as plain Markdown in git, with: a CV, links to published
papers and working papers, teaching material, and links to datasets. Nothing more — keep
scope tight.

The site does not exist yet. The full design is in
`docs/superpowers/specs/2026-05-28-website-migration-quarto-design.md` — **read it before
making structural decisions**; it records every locked decision and the rationale.

## Site owner (content source of truth)

Content must be factually accurate to Mauricio's CV. The **canonical CV is the LaTeX source
`C:\Users\mauri\Dropbox\CV\CV-ENG.tex`** (edited frequently — re-read it; do not trust this
summary for the publication list). Quick identity for context:

- Associate Professor, Centro de Investigación Económica, **ITAM**, Mexico City (2024–).
- **Co-Editor, Journal of Development Economics** (2025–).
- PhD Economics, UC San Diego (2018). BA Math + BA Economics, Universidad de los Andes.
- Fields: development, education, public, environmental economics; applied microeconometrics / RCTs.
- Affiliations: J-PAL, IPA, EGAP, CGD, BREAD, IZA. Jacobs Foundation Research Fellow (2024–26).
- Email `mtromero@itam.mx`; Google Scholar user `BD8UfDoAAAAJ`; Twitter `marome1`; Bluesky.
- Citizenship: Colombia.

**The website's publication list must stay consistent with `CV-ENG.tex`.** When in doubt
about a paper's title, coauthors, venue, or link, the CV `.tex` wins.

## Planned site structure

Four sections mirroring the current live site: Bio/CV (`index.qmd`), Research
(`research.qmd` — publications + working papers), Data & Code (`data-code.qmd`),
Teaching (`teaching.qmd`). Publications are **hand-written per-entry Markdown blocks**
(no `.bib` pipeline). Theme: clean academic Bootswatch (default `litera`/`cosmo`) +
light `styles.scss`.

## Source material (not part of the deployed site)

- `public_html/` — the WordPress FTP download (2.3 GB, **gitignored**). Reference only.
  Useful parts: `public_html/pdfs/` (733 PDFs: papers, CV, teaching notes) and
  `public_html/wp-content/uploads/` (images). WP core / DB are not migrated.
- The current page *text* lives in the WordPress MySQL database, not in files — pull it by
  reading the rendered live pages, not from `public_html/`.

## Commands

```powershell
winget install --id Posit.Quarto -e   # Quarto not yet installed; only missing tool
quarto preview                        # local live preview while editing
quarto render                         # build to _site/
```

PDF compression (target: get repo under ~1 GB for GitHub Pages):
```powershell
gswin64c -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook `
  -dNOPAUSE -dQUIET -dBATCH -sOutputFile=out.pdf in.pdf
```

Deploy is via a GitHub Action (`quarto-dev/quarto-actions`) that builds on push to `main`
and publishes to `gh-pages`; `gh` CLI (installed) manages the repo.

## Hard constraints

- **GitHub account is `mauricioromero86`.** The username `mauricioromero` is taken by
  someone else, so `mauricioromero.github.io` is unavailable — the test URL is
  **`mauricioromero86.github.io`** (user-site repo, serves at root). Final URL is the custom
  domain `mauricio-romero.com`.
- **Repo must stay under ~1 GB** (GitHub Pages soft limit). Compress PDFs first; prune oldest
  course-years only with owner approval. No single file > 100 MB.
- **SEO/AI**: implement Google's SEO + AI optimization guides (per-page title/description,
  `site-url` → auto `sitemap.xml`, Open Graph + Twitter cards, `Person`/`ProfilePage` JSON-LD,
  `robots.txt`). **Do NOT create `llms.txt` or AI-specific markup** — Google's AI guide
  explicitly advises against it.
- Domain cutover only after verifying on `*.github.io`; add a redirect on the old Bluehost
  site during the transition.

## Working conventions

- The repo root is a git repo; `public_html/`, `_site/`, `.quarto/` are gitignored.
- This is a brainstormed project under the superpowers workflow — the spec is approved before
  implementation; implementation follows a written plan (see `docs/superpowers/`).
