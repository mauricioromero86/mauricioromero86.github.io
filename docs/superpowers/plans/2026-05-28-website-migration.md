# Website Migration (WordPress → Quarto/GitHub Pages) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the WordPress/Mesmerize site at `mauricio-romero.com` with a static Quarto site on GitHub Pages — editable as plain Markdown, free, git-deployed, SEO/AI-optimized — then cut the domain over and retire Bluehost.

**Architecture:** Quarto website (4 `.qmd` pages + `_quarto.yml`) builds to static HTML via a GitHub Action that publishes to the `gh-pages` branch of the user-site repo `mauricioromero86.github.io`. Paper PDFs are kept in-repo at their exact existing `/pdfs/papers/` paths (compressed); the `polucion/` maps are migrated as-is; datasets/replication are linked externally. Custom domain via `CNAME` + DNS at cutover.

**Tech Stack:** Quarto, Bootswatch theme, GitHub Pages + Actions, `gh` CLI, Ghostscript (PDF compression), GA4. Shell is **PowerShell on Windows**.

**Source of truth for content:** `C:\Users\mauri\Dropbox\CV\CV-ENG.tex` (publications, teaching, positions) and the rendered live site `https://mauricio-romero.com` (bio prose, headshot). Cross-check every publication against the CV.

**Conventions for this plan:** "Tests" for a static site = build succeeds, expected file exists, link resolves, expected tag present in rendered HTML. Each task ends with a commit. Repo already exists at `C:\Users\mauri\Dropbox\Personal_Website` (git initialized; `public_html/`, `_site/`, `.quarto/` gitignored).

---

## File structure (what gets created)

```
Personal_Website/                 (existing git repo root → GitHub: mauricioromero86.github.io)
├── _quarto.yml                   # site config: type, theme, navbar, site-url, OG/cards, GA4
├── index.qmd                     # Bio/CV homepage + Person/ProfilePage JSON-LD
├── research.qmd                  # Publications + working papers (from CV-ENG.tex)
├── teaching.qmd                  # Courses (from CV-ENG.tex)
├── data-code.qmd                 # External dataset/replication links + polucion maps
├── styles.scss                   # accent color, fonts
├── robots.txt                    # allow all + sitemap pointer
├── _includes/person-jsonld.html  # JSON-LD structured data (included by index.qmd)
├── CNAME                         # mauricio-romero.com (added at cutover, Task 17)
├── pdfs/                         # compressed; papers/ paths preserved exactly
├── polucion/                     # 16 maps, migrated as-is
├── img/                          # headshot + favicon
└── .github/workflows/publish.yml # Quarto → gh-pages
```

---

## Phase 0 — Toolchain & repo bootstrap

### Task 1: Install Quarto

**Files:** none (local toolchain)

- [ ] **Step 1: Install Quarto**

Run (PowerShell):
```powershell
winget install --id Posit.Quarto -e --accept-source-agreements --accept-package-agreements
```

- [ ] **Step 2: Open a NEW PowerShell window, verify**

Run: `quarto --version`
Expected: a version string like `1.6.x` (a new shell is needed so PATH picks up Quarto).

- [ ] **Step 3: Verify the bundled tools**

Run: `quarto check`
Expected: `[✓]` lines for Quarto installation and Pandoc. (R/Python/LaTeX warnings are fine — not used.)

No commit (toolchain only).

---

### Task 2: Create the GitHub repo and connect the remote

**Files:** none (remote setup)

- [ ] **Step 1: Confirm gh auth**

Run: `gh auth status`
Expected: logged in as `mauricioromero86`. If not: `gh auth login` (owner runs this interactively — type `! gh auth login` in the session).

- [ ] **Step 2: Create the user-site repo**

Run:
```powershell
gh repo create mauricioromero86.github.io --public --description "Academic website of Mauricio Romero"
```
Expected: `✓ Created repository mauricioromero86/mauricioromero86.github.io on GitHub`.

- [ ] **Step 3: Add the remote to the existing local repo**

Run:
```powershell
git remote add origin https://github.com/mauricioromero86/mauricioromero86.github.io.git
git branch -M main
```
Expected: no error. Verify: `git remote -v` shows `origin`.

- [ ] **Step 4: Commit**
```powershell
git commit --allow-empty -m "chore: connect github remote for site repo"
```

---

## Phase 1 — Scaffold the Quarto site (renders with placeholder content)

### Task 3: Site config `_quarto.yml`

**Files:**
- Create: `_quarto.yml`

- [ ] **Step 1: Write `_quarto.yml`**

```yaml
project:
  type: website
  output-dir: _site

website:
  title: "Mauricio Romero"
  description: "Mauricio Romero — Associate Professor of Economics at ITAM. Development, education, and public economics."
  site-url: "https://mauricioromero86.github.io"   # switched to custom domain at cutover (Task 17)
  open-graph: true
  twitter-card: true
  google-analytics: "G-PLACEHOLDER"                 # replaced with real GA4 ID in Task 16
  favicon: img/favicon.png
  navbar:
    title: "Mauricio Romero"
    right:
      - text: "Home"
        href: index.qmd
      - text: "Research"
        href: research.qmd
      - text: "Teaching"
        href: teaching.qmd
      - text: "Data & Code"
        href: data-code.qmd
      - icon: envelope
        href: "mailto:mtromero@itam.mx"
      - icon: google
        href: "https://scholar.google.com/citations?user=BD8UfDoAAAAJ"

format:
  html:
    theme:
      - litera
      - styles.scss
    toc: false
    page-layout: full
    grid:
      body-width: 900px
```

- [ ] **Step 2: Commit** (build verified in Task 6)
```powershell
git add _quarto.yml
git commit -m "feat: add quarto site config"
```

---

### Task 4: Four pages with front matter + placeholder bodies

**Files:**
- Create: `index.qmd`, `research.qmd`, `teaching.qmd`, `data-code.qmd`

- [ ] **Step 1: Create `index.qmd`**
```markdown
---
title: "Mauricio Romero"
description: "Associate Professor of Economics at ITAM; Co-Editor, Journal of Development Economics. Development, education, and public economics."
include-in-header: _includes/person-jsonld.html
---

::: {.placeholder}
Bio prose goes here (Task 8).
:::
```

- [ ] **Step 2: Create `research.qmd`**
```markdown
---
title: "Research"
description: "Publications and working papers by Mauricio Romero in development, education, and public economics."
---

Publications and working papers (Task 9).
```

- [ ] **Step 3: Create `teaching.qmd`**
```markdown
---
title: "Teaching"
description: "Courses and teaching materials by Mauricio Romero at ITAM and elsewhere."
---

Courses (Task 10).
```

- [ ] **Step 4: Create `data-code.qmd`**
```markdown
---
title: "Data & Code"
description: "Datasets, replication packages, and interactive tools from Mauricio Romero's research."
---

Data, code, and tools (Task 11).
```

- [ ] **Step 5: Commit**
```powershell
git add index.qmd research.qmd teaching.qmd data-code.qmd
git commit -m "feat: scaffold four site pages with SEO front matter"
```

---

### Task 5: Theme styling, robots.txt, JSON-LD include

**Files:**
- Create: `styles.scss`, `robots.txt`, `_includes/person-jsonld.html`

- [ ] **Step 1: Create `styles.scss`**
```scss
/*-- scss:defaults --*/
$primary: #1a5276;          // deep academic blue (replaces Mesmerize cyan)
$body-color: #222;
$link-color: $primary;

/*-- scss:rules --*/
.navbar-title { font-weight: 600; }
body { font-size: 1.02rem; line-height: 1.6; }
h2 { margin-top: 2rem; }
```

- [ ] **Step 2: Create `robots.txt`**
```
User-agent: *
Allow: /

Sitemap: https://mauricioromero86.github.io/sitemap.xml
```
(Sitemap URL switched to the custom domain at cutover, Task 17.)

- [ ] **Step 3: Create `_includes/person-jsonld.html`**
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfilePage",
  "mainEntity": {
    "@type": "Person",
    "name": "Mauricio Romero",
    "jobTitle": "Associate Professor of Economics",
    "affiliation": {
      "@type": "Organization",
      "name": "Instituto Tecnológico Autónomo de México (ITAM)"
    },
    "email": "mailto:mtromero@itam.mx",
    "url": "https://mauricio-romero.com",
    "sameAs": [
      "https://scholar.google.com/citations?user=BD8UfDoAAAAJ",
      "https://twitter.com/marome1"
    ]
  }
}
</script>
```

- [ ] **Step 4: Commit**
```powershell
git add styles.scss robots.txt _includes/person-jsonld.html
git commit -m "feat: theme styling, robots.txt, Person JSON-LD"
```

---

### Task 6: First local build (verification gate)

**Files:** none (produces `_site/`, gitignored)

- [ ] **Step 1: Render the site**

Run: `quarto render`
Expected: `Output created: _site/index.html` and no errors.

- [ ] **Step 2: Verify all four pages built**

Run (PowerShell):
```powershell
Get-ChildItem _site\*.html | Select-Object Name
```
Expected: `index.html`, `research.html`, `teaching.html`, `data-code.html`.

- [ ] **Step 3: Verify sitemap + JSON-LD generated**

Run:
```powershell
Test-Path _site\sitemap.xml
Select-String -Path _site\index.html -Pattern "ProfilePage" -Quiet
```
Expected: `True` and `True`.

- [ ] **Step 4: Eyeball it**

Run: `quarto preview` → open the local URL it prints. Confirm navbar, four pages, theme. Stop preview (Ctrl+C).

No commit (no source change). If `_quarto.yml`/pages needed fixes, commit those.

---

## Phase 2 — Content (real text from CV + live site)

### Task 7: Recover live-site page text

**Files:** Create: `docs/superpowers/migration-notes/live-content.md` (scratch reference, committed)

- [ ] **Step 1: Capture each live page's text + SEO tags**

For each of the four live URLs (home, and the Research/Teaching/Data pages — discover exact slugs from the live navbar), fetch and save the visible text and the `<title>`/`<meta name="description">`. Use WebFetch per page, or:
```powershell
@("https://mauricio-romero.com/") | ForEach-Object {
  Invoke-WebRequest $_ -UseBasicParsing | Select-Object -ExpandProperty Content |
  Out-File "docs/superpowers/migration-notes/home.html" -Encoding utf8
}
```
Record the page slugs (e.g. `/research`, `/teaching`) — needed for redirects in Task 19.

- [ ] **Step 2: Distill into `live-content.md`**

Write the recovered bio prose, section text, and the existing SEO title/description per page into `live-content.md`. This is the raw material for Tasks 8–11. Note anything present on the live site but absent from the CV.

- [ ] **Step 3: Commit**
```powershell
git add docs/superpowers/migration-notes/
git commit -m "docs: recovered live-site content for migration"
```

---

### Task 8: Bio/CV homepage (`index.qmd`)

**Files:** Modify: `index.qmd`

- [ ] **Step 1: Write the bio body**

Replace the placeholder with prose assembled from `live-content.md` + CV header facts. Required elements (all verifiable from `CV-ENG.tex`):
- Position: Associate Professor, Centro de Investigación Económica, ITAM (2024–); Co-Editor, *Journal of Development Economics* (2025–).
- Education: PhD Economics, UC San Diego (2018); BA Math + BA Economics, Universidad de los Andes.
- Research focus sentence (from live site): bottlenecks impeding high-quality government provision of education, health care, and environmental protection.
- Affiliations line: J-PAL, IPA, EGAP, CGD, BREAD, IZA.
- Honors line: Jacobs Foundation Research Fellow (2024–26); LACEA Executive Committee (2024–27).
- Links row: CV PDF (`pdfs/Mauricio-Romero-CV.pdf`), Google Scholar (`user=BD8UfDoAAAAJ`), email `mtromero@itam.mx`, Twitter `marome1`, Bluesky.
- Headshot via `![Mauricio Romero](img/headshot.jpg){width=220px .rounded}` (file added in Task 14) with descriptive alt text.

- [ ] **Step 2: Render + verify**

Run: `quarto render index.qmd`
Run: `Select-String -Path _site\index.html -Pattern "Journal of Development Economics" -Quiet`
Expected: render succeeds; pattern `True`.

- [ ] **Step 3: Commit**
```powershell
git add index.qmd
git commit -m "feat: bio/CV homepage content"
```

---

### Task 9: Research page (`research.qmd`)

**Files:** Modify: `research.qmd`

> The `add-publication` project skill encodes the canonical block format and sources details from `CV-ENG.tex`. Use it to generate entries, or transcribe directly.

- [ ] **Step 1: Define the section structure**

Add these `##` sections, in this order, matching `CV-ENG.tex`: **Publications (peer-reviewed)**, **Comments, conference proceedings, and others**, **Non-econ peer-reviewed articles**, **Working papers**, **Research in progress**, **Resting papers**.

- [ ] **Step 2: Transcribe every entry from `CV-ENG.tex`**

For each paper in the corresponding CV section, write one block in this exact format:
```markdown
### {Title}
*with {coauthors}* · *{Journal}*, {Year}   <!-- or "Revise and resubmit at …" / "Forthcoming in …" -->

[Journal]({doi-or-publisher-url}) · [PDF]({link})
```
Rules:
- **Published papers:** use the journal/DOI URL from the CV as `[Journal]`.
- **Working/resting papers:** the CV links them to `https://mauricio-romero.com/pdfs/papers/<file>.pdf` — keep these as **root-relative** `/pdfs/papers/<file>.pdf` so they resolve on the new site (path preserved in Task 12).
- Two concrete worked examples (verify against CV):
```markdown
### Inputs, Incentives, and Complementarities in Primary Education: Experimental Evidence from Tanzania
*with Karthik Muralidharan, Isaac Mbiti, Youdi Schipper, Constantine Mandak, Rakesh Rajani* · *Quarterly Journal of Economics* 134(3), 2019

[Journal](https://academic.oup.com/qje/article/134/3/1627/5479257)

### The incidence of affirmative action: Evidence from quotas in private schools in India
*with Abhijeet Singh* · Revise and resubmit at the *Review of Economic Studies*

[PDF](/pdfs/papers/CG_RTE_Draft.pdf)
```

- [ ] **Step 3: Render + verify entry count matches the CV**

Run: `quarto render research.qmd`
Run (count `###` entries):
```powershell
(Select-String -Path research.qmd -Pattern "^### " ).Count
```
Expected: equals the total paper count across the six CV sections (15 peer-reviewed + 2 comments + 2 non-econ + 2 working + 6 in-progress + 3 resting at time of writing — re-verify against current `CV-ENG.tex`).

- [ ] **Step 4: Commit**
```powershell
git add research.qmd
git commit -m "feat: research page (publications + working papers from CV)"
```

---

### Task 10: Teaching page (`teaching.qmd`)

**Files:** Modify: `teaching.qmd`

- [ ] **Step 1: Write course sections from the CV "Teaching experience" section**

Group by institution. For ITAM list each course with terms taught and link to its materials folder (paths preserved in Task 12), e.g.:
```markdown
## ITAM

### Economics IV
Fall 2018 – Fall 2025. [Materials](/pdfs/EcoIV/)

### Microeconometrics (causal inference & impact evaluation)
Fall 2020 – Spring 2026. [Materials](/pdfs/Microeconometria/)

### Seminario de Análisis Empírico
Spring 2026. [Materials](/pdfs/AnalisisEmpirico/)
```
Then shorter entries for J-PAL, EGAP, University of Bern, Universidad de los Andes, Universidad del Rosario (no links unless a PDF exists in `pdfs/`).

- [ ] **Step 2: Render + verify**

Run: `quarto render teaching.qmd`
Run: `Select-String -Path _site\teaching.html -Pattern "Microeconometrics" -Quiet`
Expected: render succeeds; `True`.

- [ ] **Step 3: Commit**
```powershell
git add teaching.qmd
git commit -m "feat: teaching page from CV"
```

---

### Task 11: Data & Code page (`data-code.qmd`)

**Files:** Modify: `data-code.qmd`

- [ ] **Step 1: Write the page with two sections**

```markdown
## Replication packages & data

Replication materials are hosted in public data repositories:

- **Inputs, Incentives, and Complementarities (QJE 2019)** — [replication package]({QJE_archive_url})
- **{paper}** — [replication package]({archive_url})

(Repository URLs filled in Step 2.)

## Interactive tools

### Air quality in Bogotá
Neighborhood-level pollution maps:
[Usaquén](/polucion/usaquen.html) · [Suba](/polucion/suba.html) · [Kennedy](/polucion/kennedy.html) · … (all 16)
```

- [ ] **Step 2: Resolve the external repository URLs (owner action)**

For each replication zip in `public_html/replicationData/`, get its public archive URL: prefer the **journal's official replication archive** (AEA/Dataverse/ICPSR) or the journal article's data link; if none exists, upload the zip to **Zenodo or OSF** and use the resulting DOI/URL. Record each URL and substitute into the `{archive_url}` slots. Do **not** commit the zips to the repo.

- [ ] **Step 3: Render + verify the polucion links resolve locally**

Run: `quarto render data-code.qmd` (after Task 13 copies `polucion/`).
Run: `Test-Path _site\polucion\usaquen.html`
Expected: `True`.

- [ ] **Step 4: Commit**
```powershell
git add data-code.qmd
git commit -m "feat: data & code page (external links + polucion maps)"
```

---

## Phase 3 — Assets

### Task 12: Compress PDFs and copy into the repo (paths preserved)

**Files:** Create: `pdfs/` (subset of `public_html/pdfs/`, compressed), `tools/compress-pdfs.ps1`

- [ ] **Step 1: Confirm Ghostscript is available**

Run: `gswin64c --version`
Expected: a version number. If missing: `winget install --id ArtifexSoftware.GhostScript -e`, then open a new shell.

- [ ] **Step 2: Write `tools/compress-pdfs.ps1`**
```powershell
param([string]$Src, [string]$Dst)
Get-ChildItem -Path $Src -Recurse -Filter *.pdf | ForEach-Object {
  $rel = $_.FullName.Substring((Resolve-Path $Src).Path.Length).TrimStart('\')
  $out = Join-Path $Dst $rel
  New-Item -ItemType Directory -Force -Path (Split-Path $out) | Out-Null
  & gswin64c -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook `
    -dNOPAUSE -dQUIET -dBATCH -sOutputFile=$out $_.FullName
  # keep whichever is smaller (compression can occasionally inflate)
  if ((Get-Item $out).Length -ge $_.Length) { Copy-Item $_.FullName $out -Force }
}
```

- [ ] **Step 3: Compress papers + CV first (small, always kept)**
```powershell
.\tools\compress-pdfs.ps1 -Src "public_html\pdfs\papers" -Dst "pdfs\papers"
Copy-Item "public_html\pdfs\Mauricio-Romero-CV.pdf" "pdfs\Mauricio-Romero-CV.pdf"
```
Verify a known external path is preserved: `Test-Path pdfs\papers\CG_RTE_Draft.pdf` → `True`.

- [ ] **Step 4: Compress teaching folders, then check total size**
```powershell
foreach ($c in "EcoIV","Microeconometria","Inferencia","AnalisisEmpirico","FieldExperiments","TeoJuegos201319","TeoJuegos201419","MicroII201819","MicroIII201619") {
  .\tools\compress-pdfs.ps1 -Src "public_html\pdfs\$c" -Dst "pdfs\$c"
}
"{0:N0} MB" -f ((Get-ChildItem pdfs -Recurse | Measure-Object Length -Sum).Sum/1MB)
```
Expected: report total. **If over ~900 MB**, prune oldest course-years (owner approves): remove `pdfs\EcoIV\20201`, `pdfs\EcoIV\20211`, `pdfs\EcoIV\PastExams` first (the 1 GB of the 1.8 GB), re-measure. Repeat until under ~900 MB.

- [ ] **Step 5: Commit** (this is the large commit)
```powershell
git add pdfs tools/compress-pdfs.ps1
git commit -m "feat: compressed PDFs (papers paths preserved) + teaching materials"
```

---

### Task 13: Migrate `polucion/` and the headshot/favicon

**Files:** Create: `polucion/` (copy), `img/headshot.jpg`, `img/favicon.png`

- [ ] **Step 1: Copy polucion as-is**
```powershell
Copy-Item "public_html\polucion" "polucion" -Recurse
```
Verify: `(Get-ChildItem polucion\*.html).Count` → `16`.

- [ ] **Step 2: Obtain the headshot**

Download the professor's photo from the live site's media library (inspect the homepage `<img>` from Task 7's saved HTML for its URL), save as `img/headshot.jpg`. If not found on the live site, request it from the owner. Create a `img/favicon.png` (square crop or initials).

- [ ] **Step 3: Verify and commit**
```powershell
Test-Path img\headshot.jpg
git add polucion img
git commit -m "feat: migrate polucion maps + add headshot/favicon"
```

---

### Task 14: Full build + link verification

**Files:** Create: `tools/check-links.ps1`

- [ ] **Step 1: Write `tools/check-links.ps1`** (checks every local href in `_site` resolves)
```powershell
$root = "_site"
$bad = @()
Get-ChildItem $root -Recurse -Filter *.html | ForEach-Object {
  $html = Get-Content $_.FullName -Raw
  [regex]::Matches($html, 'href="(/[^":#?]+)') | ForEach-Object {
    $p = $_.Groups[1].Value
    $fs = Join-Path $root ($p -replace '/', '\')
    if (-not (Test-Path $fs) -and -not (Test-Path "$fs.html") -and -not (Test-Path (Join-Path $fs 'index.html'))) {
      $bad += "$($_.Groups[1].Value)  (in $($_.Name))"
    }
  }
}
if ($bad) { $bad | Sort-Object -Unique; "FAIL: $($bad.Count) broken local links" } else { "OK: all local links resolve" }
```

- [ ] **Step 2: Render and run the checker**

Run: `quarto render`
Run: `.\tools\check-links.ps1`
Expected: `OK: all local links resolve`. Fix any broken `/pdfs/...` or `/polucion/...` paths in the `.qmd` files, re-render, re-run.

- [ ] **Step 3: Commit**
```powershell
git add tools/check-links.ps1
git commit -m "test: local link checker; all links resolve"
```

---

## Phase 4 — Deploy to github.io (verification before cutover)

### Task 15: GitHub Action + GA4

**Files:** Create: `.github/workflows/publish.yml`; Modify: `_quarto.yml`

- [ ] **Step 1: Create GA4 property (owner action)**

In Google Analytics, create a GA4 property for the site; copy the Measurement ID (`G-XXXXXXXXXX`).

- [ ] **Step 2: Put the real GA4 ID in `_quarto.yml`**

Replace `google-analytics: "G-PLACEHOLDER"` with the real ID.

- [ ] **Step 3: Create `.github/workflows/publish.yml`**
```yaml
on:
  workflow_dispatch:
  push:
    branches: main

name: Quarto Publish

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - name: Check out repository
        uses: actions/checkout@v4
      - name: Set up Quarto
        uses: quarto-dev/quarto-actions/setup@v2
      - name: Render and Publish
        uses: quarto-dev/quarto-actions/publish@v2
        with:
          target: gh-pages
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

- [ ] **Step 4: Commit**
```powershell
git add .github/workflows/publish.yml _quarto.yml
git commit -m "ci: quarto publish workflow + GA4 id"
```

---

### Task 16: Push and publish

**Files:** none

- [ ] **Step 1: Push main**

Run: `git push -u origin main`
Expected: push succeeds; the `Quarto Publish` Action starts.

- [ ] **Step 2: Watch the Action**

Run: `gh run watch`
Expected: workflow completes ✓ and creates the `gh-pages` branch.

- [ ] **Step 3: Set Pages source to `gh-pages` (required for user sites)**

Run:
```powershell
gh api -X POST repos/mauricioromero86/mauricioromero86.github.io/pages -f source[branch]=gh-pages -f source[path]=/ 2>$null; if (-not $?) { gh api -X PUT repos/mauricioromero86/mauricioromero86.github.io/pages -f source[branch]=gh-pages -f source[path]=/ }
```
Or in the browser: Settings → Pages → Source → Deploy from a branch → `gh-pages` / `/ (root)`. Also ensure Settings → Actions → Workflow permissions = "Read and write".

- [ ] **Step 4: Verify the live test site**

Wait ~1–2 min, then run:
```powershell
(Invoke-WebRequest "https://mauricioromero86.github.io/" -UseBasicParsing).StatusCode
```
Expected: `200`. Open it; click through all four pages, a paper PDF (`/pdfs/papers/...`), and a polucion map.

No commit.

---

### Task 17: SEO/structured-data verification on the live test site

**Files:** none

- [ ] **Step 1: Verify sitemap, robots, titles**

Run:
```powershell
(Invoke-WebRequest "https://mauricioromero86.github.io/sitemap.xml" -UseBasicParsing).StatusCode
(Invoke-WebRequest "https://mauricioromero86.github.io/robots.txt" -UseBasicParsing).StatusCode
```
Expected: both `200`.

- [ ] **Step 2: Verify per-page unique titles/descriptions and OG/Twitter tags**
```powershell
"index","research","teaching","data-code" | ForEach-Object {
  $u = if ($_ -eq "index") { "https://mauricioromero86.github.io/" } else { "https://mauricioromero86.github.io/$_.html" }
  $h = (Invoke-WebRequest $u -UseBasicParsing).Content
  "$_  title=$([regex]::Match($h,'<title>(.*?)</title>').Groups[1].Value)  ogdesc=$([bool][regex]::Match($h,'og:description'))"
}
```
Expected: a distinct title per page; `ogdesc=True` each.

- [ ] **Step 3: Validate JSON-LD**

Paste `https://mauricioromero86.github.io/` into Google's Rich Results Test (search.google.com/test/rich-results). Expected: `ProfilePage`/`Person` detected, no errors.

No commit (verification only). Fix + re-push if anything fails.

---

## Phase 5 — Domain cutover & decommission (gated on Phase 4 verified)

### Task 18: Switch site-url/robots/sitemap to the custom domain + add CNAME

**Files:** Create: `CNAME`; Modify: `_quarto.yml`, `robots.txt`

- [ ] **Step 1: Add `CNAME`** (file content is exactly the apex domain)
```
mauricio-romero.com
```

- [ ] **Step 2: Update `_quarto.yml`** — `site-url: "https://mauricio-romero.com"`.

- [ ] **Step 3: Update `robots.txt`** — `Sitemap: https://mauricio-romero.com/sitemap.xml`.

- [ ] **Step 4: Commit + push**
```powershell
git add CNAME _quarto.yml robots.txt
git commit -m "feat: custom domain (CNAME + site-url)"
git push
```
Wait for the Action to finish (`gh run watch`).

---

### Task 19: DNS records (owner action at registrar/Bluehost DNS)

**Files:** none

- [ ] **Step 1: Point the apex domain to GitHub Pages**

In the DNS manager for `mauricio-romero.com`, set **A** records for `@` to:
`185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
and a **CNAME** for `www` → `mauricioromero86.github.io`.
Remove the old Bluehost A record.

- [ ] **Step 2: Verify DNS + HTTPS**

After propagation (minutes–hours):
```powershell
nslookup mauricio-romero.com
```
Expected: resolves to the `185.199.*` IPs. Then in Settings → Pages, confirm the custom domain shows green and tick **Enforce HTTPS** (wait for the cert to issue).
```powershell
(Invoke-WebRequest "https://mauricio-romero.com/" -UseBasicParsing).StatusCode
(Invoke-WebRequest "https://mauricio-romero.com/pdfs/papers/CG_RTE_Draft.pdf" -UseBasicParsing).StatusCode
```
Expected: both `200` (the second confirms preserved paper URLs work on the real domain).

---

### Task 20: Search Console + sitemap submission

**Files:** none (owner action)

- [ ] **Step 1: Verify the domain** in Google Search Console (DNS TXT or the existing site). **Step 2:** Submit `https://mauricio-romero.com/sitemap.xml`. Confirm it's read with no errors.

---

### Task 21: Transition redirect on the OLD Bluehost site, then decommission

**Files:** Modify (on Bluehost, not in this repo): `public_html/.htaccess` or `index.php`

> Note: once DNS points at GitHub Pages (Task 19), the apex domain already serves the new site, so this redirect only matters during the brief window before DNS propagates and for anyone hitting the Bluehost IP directly. Apply it before/at cutover.

- [ ] **Step 1: Add a redirect on Bluehost** — via SFTP, prepend to `public_html/.htaccess`:
```apache
RewriteEngine On
RewriteCond %{HTTP_HOST} !^mauricioromero86\.github\.io$ [NC]
RewriteRule ^(.*)$ https://mauricio-romero.com/$1 [R=301,L]
```
(Or, simplest: a root `index.html` with `<meta http-equiv="refresh" content="0; url=https://mauricio-romero.com/">`.)

- [ ] **Step 2: Final verification window**

Confirm `https://mauricio-romero.com/` serves the new Quarto site and key URLs (home, research, a paper PDF, a polucion map) all return `200` over HTTPS for ~1 week.

- [ ] **Step 3: Decommission Bluehost** (owner) — after the verification window and after exporting anything still needed (the WP DB if not already), cancel Bluehost hosting. Keep domain registration wherever DNS is now managed.

---

## Verification criteria (whole project)

- All four pages render locally (`quarto render`) and on the live domain.
- `tools/check-links.ps1` → `OK`; every `/pdfs/papers/<file>.pdf` resolves on `mauricio-romero.com` (no broken external citations).
- Repo (and published site) under ~1 GB.
- `sitemap.xml` + `robots.txt` return `200`; each page has a unique title + description + OG/Twitter tags; homepage passes the Rich Results Test for `Person`/`ProfilePage`.
- `polucion/` maps load; `Map_IPS.html` intentionally absent.
- Publication count on `research.qmd` equals the CV's; spot-check titles/coauthors/links against `CV-ENG.tex`.
- HTTPS enforced on the custom domain; old Bluehost site redirects to it.
```
