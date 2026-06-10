# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

Migration of Mauricio Romero's academic website from **WordPress/Mesmerize on Bluehost**
(`https://mauricio-romero.com`) to a **static Quarto site on GitHub Pages**. The goal is an
academic site that is editable as plain Markdown in git, with: a CV, links to published
papers and working papers, teaching material, and links to datasets. Nothing more — keep
scope tight.

The site is live at `https://mauricio-romero.com` (custom domain cut over; GA4
`G-JM6020WT15`). The locked design decisions are in
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
Teaching (`teaching.qmd`), plus post-launch additions: a CDMX visitor guide (`cdmx.qmd`),
course pages under `courses/`, and a branded `404.qmd`. Publications are **hand-written per-entry Markdown blocks**
(no `.bib` pipeline). Theme: clean academic Bootswatch (default `litera`/`cosmo`) +
light `styles.scss`.

**Data & Code** page links *out* to externally hosted datasets and replication packages
(Dataverse/OSF/Zenodo or journal archives — `data/` and `replicationData/` are not committed)
and hosts the migrated `polucion/` maps in-repo. `Map_IPS.html` is omitted (deferred rebuild).

## Machine-readable papers (LLM-legible versions)

Papers served at `/pdfs/papers/<name>.pdf` get a clean **Markdown twin** at
`/pdfs/papers/<name>.pdf.md` (Quentin André's "append `.md` to the URL" convention,
https://quentinandre.net/posts/legible-to-machines/). Coverage as of 2026-06-10: 21 of 33
PDFs have twins; the rest are mostly appendices/supplements (backfill with `--all` is optional). PDFs are layout instructions, not
text; the `.md` is what LLMs actually read. Each `.md` has YAML front matter
(title, authors, venue, year, **real DOI**, canonical URLs) + the full converted body.

- **Source of truth for metadata:** `research.qmd` (titles, coauthors, venue, DOI from the
  BibTeX block, abstract). `tools/paper_metadata.py` parses it; both other tools import it.
- **Converter:** `tools/pdf-to-md.py` (PowerShell wrapper `tools/convert-paper-md.ps1`).
  Default engine **Marker** (`pip install -r requirements-md.txt`); add `--use-llm` (needs
  an LLM API key, e.g. `GEMINI_API_KEY`) for the highest-quality refinement pass. For the
  ~7 papers with local LaTeX source, prefer `--engine pandoc --tex <main.tex>` (perfect math).
  Figure images are intentionally **not** extracted (LLMs can't read PNGs; keeps repo small).
  - **Whole-corpus runs use Marker's batch/folder mode** (`--all`): ONE process, Surya models
    loaded once, walks the folder. Do **not** spawn one `marker_single` per paper in parallel —
    several concurrent model loads exhaust the Windows **page file** (`OSError 1455`), and each
    call otherwise re-loads the models (~minutes wasted). `--jobs N` sets the batch worker count
    *inside* that single process; keep it modest (2–3). This box is **CPU-only** (no CUDA), so
    expect tens of minutes per paper — run `--all` in the background.
- **CV:** the CV twin `pdfs/Mauricio-Romero-CV.pdf.md` is built from the **LaTeX source**
  (`C:\Users\mauri\Dropbox\CV\CV-ENG.tex`) via `python tools/pdf-to-md.py --cv` (pandoc, then
  artifact cleanup). Rebuild it whenever the CV changes. It is listed at the top of `llms.txt`
  and linked from `index.qmd`. (LaTeX → Markdown is far cleaner than converting the CV PDF.)
- **Index:** `tools/gen-llms-txt.py` regenerates root `llms.txt` (CV first, then papers that
  have a `.pdf.md`). The Research page also shows a per-entry `[Markdown]` link as the on-page
  signal; `index.qmd` links the CV's Markdown twin.
- **Committed, not CI-generated:** the `.md` and `llms.txt` are committed; the GitHub Action
  only renders/publishes. Quarto copies `/pdfs/**` and root `/llms.txt` verbatim (they are not
  in the `project: render:` list, so they are resources, not rendered inputs).
- **Adding a paper:** the `add-publication` skill runs the converter, then
  `tools/add-md-links.py` (idempotent on-page `[Markdown]` links for papers whose `.pdf.md`
  exists) + `tools/gen-llms-txt.py`. Re-run the converter if a PDF is updated.
- **Backfill note:** this box is CPU-only, so `--all` is slow (~1 hr/paper). Run it in the
  background, then re-run `tools/add-md-links.py` + `tools/gen-llms-txt.py` to wire whatever
  finished. Both are idempotent and only touch papers whose `.pdf.md` is on disk.

## Source material (not part of the deployed site)

`public_html/` is the full WordPress FTP download (**~3.3 GB of content assets, gitignored**).
Reference only — WP core/plugins/DB are not migrated. Verified inventory:

| Path | Size | What / disposition |
|------|------|--------------------|
| `pdfs/` | 2.3 GB | Teaching notes + `pdfs/papers/` (51 MB, 32 papers) + CV. EcoIV alone = **1.8 GB** |
| `data/` | 586 MB | Health/education datasets (CSV, `.dta`, SISMED/IPS) — **link externally**, not in repo |
| `replicationData/` | 271 MB | 4 replication zips (incl. one 224 MB) — **link externally** |
| `polucion/` | 44 MB | 16 self-contained Bogotá pollution maps (Pandoc/Leaflet) — **migrate as-is** |
| `Map_IPS.html` | 82 MB | Interactive health-provider map, **broken deps** — **dropped** (defer rebuild) |
| `wp-content/uploads/` | 2.2 MB | Mostly cache/config JSON; no headshot here |

- Page *text*, SEO titles/descriptions, and the **headshot** live only in the MySQL DB
  (`maurico8_WPFIY`) / media library — **not in the FTP files**. See "Recovering page content".
- Current SEO is dynamic via the **All-in-One SEO Pack** plugin; there is no `robots.txt` or
  `sitemap.xml` in the files. Analytics is a legacy Google **UA** property (deprecated → use
  GA4 or omit).
- Active theme is **Mesmerize v1.6.112** (fonts Muli + Open Sans; primary cyan `#03a9f4`) —
  reference only; we use a clean academic theme, not a replica.
- Stale duplicate `CV-ENG.pdf` copies exist under `pdfs/Microeconometria/` and
  `pdfs/TeoJuegos201419/` — ignore them; canonical CV is `C:\Users\mauri\Dropbox\CV\CV-ENG.tex`.

## Commands

```powershell
quarto preview                        # local live preview while editing
quarto render                         # build to _site/

# Machine-readable paper versions (see "Machine-readable papers" below)
python tools/pdf-to-md.py --all       # convert every paper PDF -> .pdf.md (Marker, batch)
python tools/pdf-to-md.py --all --use-llm   # + LLM refinement pass (needs API key)
python tools/pdf-to-md.py --cv        # (re)build CV twin from CV-ENG.tex (pandoc)
python tools/gen-llms-txt.py          # regenerate root llms.txt index (CV + papers)
```

**Build gotchas (Quarto installed v1.9.38):**
- **PATH:** shells started before the install don't see `quarto`. Use the absolute path
  `& "C:\Program Files\Quarto\bin\quarto.exe"` (subagents must do this) until a fresh shell.
- **Dropbox locks:** the repo is under Dropbox, which locks `.quarto/` mid-sync and breaks
  Quarto's post-render finalization (sitemap/resource copy). `.quarto/` and `_site/` are
  marked Dropbox-ignored (`Set-Content -Path .quarto -Stream com.dropbox.ignored -Value 1`).
  Keep them ignored; if a render exits 1 only on a `_freeze`/temp `remove (os error 32)`, the
  HTML still built — re-run after the ignore propagates.
- **Render scope:** `_quarto.yml` has an explicit `project: render:` list (`index`, `research`, `teaching`, `data-code`, `cdmx`, `courses/*.qmd`, `404`).
  Without it Quarto walks the whole tree (incl. `public_html/`) and tries to execute
  teaching `.qmd` files. Do not remove the render list.

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
- **Repo must stay under ~1 GB** (GitHub Pages soft limit). The source is ~3.3 GB. Fit
  strategy: link `data/` + `replicationData/` (~860 MB) out of the repo, then
  compress/prune teaching PDFs. Prune/compress targets: **EcoIV (1.8 GB)** — esp. terms
  `20201` (363 MB), `20211` (449 MB), and `PastExams` (184 MB). No single file > 100 MB.
- **URL preservation (SEO)**: keep paper PDFs at their exact existing paths
  `/pdfs/papers/<file>.pdf` — they are cited from the CV and external sites. GitHub Pages has
  **no server-side 301s**, so paths must match (or use client-side redirects). Preserve
  `/polucion/*.html` paths too if kept.
- **SEO/AI**: implement Google's SEO + AI optimization guides (per-page title/description,
  `site-url` → auto `sitemap.xml`, Open Graph + Twitter cards, `Person`/`ProfilePage` JSON-LD,
  `robots.txt`). **Maintain a root `llms.txt`** indexing the machine-readable paper
  versions (see "Machine-readable papers" below) — it is generated by
  `tools/gen-llms-txt.py`, not hand-edited. *(This reverses the earlier "no llms.txt"
  rule: the owner opted in, following Quentin André's "legible to machines" approach.
  Google's crawlers may ignore `llms.txt`, but it is cheap, harmless, and used by other
  agents.)* Still **do not** add other AI-specific markup beyond `llms.txt` + the served
  `.md` files.
- Domain cutover only after verifying on `*.github.io`; add a redirect on the old Bluehost
  site during the transition.

## Recovering page content

The four pages' text, their All-in-One-SEO titles/descriptions, and the headshot are **not in
the FTP download** — they live in the WordPress DB / media library. To migrate them:

- **Preferred**: scrape the rendered live pages (Bio/CV, Research, Data & Code, Teaching) from
  `https://mauricio-romero.com` and their `<title>`/`<meta name="description">` tags.
- **Or**: export the DB (`maurico8_WPFIY`) via phpMyAdmin / `wp db export` for the raw text.
- The headshot must be pulled from the live media library or requested from the owner.
- Cross-check every recovered publication against `CV-ENG.tex` before publishing.

## Working conventions

- The repo root is a git repo; `public_html/`, `_site/`, `.quarto/` are gitignored.
- This is a brainstormed project under the superpowers workflow — the spec is approved before
  implementation; implementation follows a written plan (see `docs/superpowers/`).
