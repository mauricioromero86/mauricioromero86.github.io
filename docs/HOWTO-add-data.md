# How to add a dataset to the website

The website is a static GitHub Pages site, so it cannot store large files in the repo itself
(GitHub blocks any file > 100 MB and the repo must stay under ~1 GB). The pattern is:

1. **Small files (< ~25 MB, and you want them in version control):** commit them to the repo
   under `data/` and link with a root-relative path.
2. **Large files / datasets (the usual case):** upload them as **GitHub Release assets** (no
   size cap that matters here — 2 GB per file), then link to the asset URL. This is the same
   mechanism the site already uses for teaching PDFs (`teaching-archive`) and research data
   (`data-archive`).

This doc covers the Release path (option 2), which is what you want for research datasets.

---

## One-time concepts

- A **Release** is a named bucket of files attached to a git tag. We use one Release per
  category: `teaching-archive` (course PDFs/code) and `data-archive` (research datasets).
- Each uploaded file becomes an **asset** with a stable, public URL:
  `https://github.com/mauricioromero86/mauricioromero86.github.io/releases/download/<TAG>/<ASSET_NAME>`
- Asset names can't contain spaces, so we flatten the original path:
  `data/sismed/2016.csv` → asset `data_sismed_2016.csv`.

Prerequisites: the `gh` CLI (already installed) authenticated as `mauricioromero86`
(`gh auth status` to check).

---

## Adding new data — step by step

### Step 1 — Put the files somewhere on disk
Collect the files you want to publish in a folder, e.g. `C:\Users\mauri\Dropbox\Personal_Website\public_html\data\<newset>\`.
(`public_html/` is git-ignored, so it never bloats the repo.)

### Step 2 — Stage + upload to the Release
The repo has a script that flattens names, writes a manifest, and uploads. To add a new folder,
edit the `$dirs` array in `tools/stage-data.ps1` to include your new subfolder, then run:

```powershell
cd C:\Users\mauri\Dropbox\Personal_Website
# dry run: stage + build the manifest only (no upload)
powershell -NoProfile -ExecutionPolicy Bypass -File tools\stage-data.ps1
# upload to the data-archive Release (creates it if missing)
powershell -NoProfile -ExecutionPolicy Bypass -File tools\stage-data.ps1 -Upload
```

This writes `docs/superpowers/migration-notes/data-manifest.csv` with one row per file:
`OrigPath, Asset, Url, Bytes, Name`. The `Url` column is the public download link.

> Manual alternative (single file, no script):
> ```powershell
> gh release upload data-archive "C:\path\to\myfile.csv" --repo mauricioromero86/mauricioromero86.github.io --clobber
> # URL becomes: https://github.com/mauricioromero86/mauricioromero86.github.io/releases/download/data-archive/myfile.csv
> ```
> If the Release doesn't exist yet:
> ```powershell
> gh release create data-archive --repo mauricioromero86/mauricioromero86.github.io --title "Research data archive" --notes "..."
> ```

### Step 3 — Confirm the asset resolves
```powershell
curl.exe -s -o NUL -w "%{http_code}`n" -L "https://github.com/mauricioromero86/mauricioromero86.github.io/releases/download/data-archive/data_sismed_2016.csv"
```
Expect `200`.

### Step 4 — Add the link to the page
Edit `data-code.qmd` and add a Markdown link using the `Url` from the manifest:

```markdown
- [SISMED 2016 (CSV)](https://github.com/mauricioromero86/mauricioromero86.github.io/releases/download/data-archive/data_sismed_2016.csv)
```

### Step 5 — Build, commit, deploy
```powershell
& "C:\Program Files\Quarto\bin\quarto.exe" render data-code.qmd   # smoke test
git add data-code.qmd docs\superpowers\migration-notes\data-manifest.csv tools\stage-data.ps1
git commit -m "data: add <newset> to data-archive and link on Data & Code"
git push origin main        # GitHub Action rebuilds and publishes
```

The live page updates a minute or two after CI finishes.

---

## Small-file alternative (commit to repo)

For a handful of small files you want under version control:

```powershell
# put files under data/ (NOT public_html/), e.g. data/class/mydata.csv
git add data\class\mydata.csv
git commit -m "data: add mydata.csv"
git push
```
Then link with a root-relative path: `[mydata.csv](/data/class/mydata.csv)`.
Note: `data/` is currently git-ignored via the `public_html/` rule only — top-level `data/`
is NOT ignored, so this works. Keep individual files well under 100 MB.

---

## When to use Zenodo instead

For datasets you want **citable** (a DOI, a fixed version, a license), deposit on Zenodo
(<https://zenodo.org>) or Harvard Dataverse instead of a GitHub Release, then link the DOI.
Published-paper replication packages already live on Dataverse/Zenodo and are linked at the top
of `data-code.qmd`. Use a Release (this doc) for loose/raw data and convenience downloads.
