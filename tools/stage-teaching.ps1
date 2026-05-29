# Dedup teaching PDFs by content, stage unique files with collision-safe names for upload
# as GitHub Release assets, and emit a manifest (every original path -> shared asset URL).
param(
  [string]$Src   = "public_html\pdfs",
  [string]$Stage = "$env:TEMP\release-teaching",
  [string]$Manifest = "docs\superpowers\migration-notes\teaching-manifest.csv",
  [string]$Repo  = "mauricioromero86/mauricioromero86.github.io",
  [string]$Tag   = "teaching-archive"
)

$courses = "EcoIV","Microeconometria","Inferencia","AnalisisEmpirico","FieldExperiments",
           "TeoJuegos201319","TeoJuegos201419","MicroII201819","MicroIII201619"
$baseUrl = "https://github.com/$Repo/releases/download/$Tag"

New-Item -ItemType Directory -Force -Path $Stage | Out-Null
$srcRoot = (Resolve-Path $Src).Path
$byHash = @{}      # hash -> assetName (first occurrence wins)
$rows = @()

foreach ($c in $courses) {
  $cdir = Join-Path $Src $c
  if (-not (Test-Path $cdir)) { continue }
  Get-ChildItem $cdir -Recurse -Filter *.pdf | ForEach-Object {
    $rel  = $_.FullName.Substring($srcRoot.Length).TrimStart('\')   # e.g. EcoIV\20211\Lecture1.pdf
    $parts = $rel -split '\\'
    $course = $parts[0]
    $term  = if ($parts.Count -ge 3) { $parts[1] } else { "" }
    $hash  = (Get-FileHash $_.FullName -Algorithm MD5).Hash
    if (-not $byHash.ContainsKey($hash)) {
      # collision-safe asset name = flattened relative path, sanitized
      $asset = ($rel -replace '[\\/ ]','_') -replace '[^A-Za-z0-9._-]','_'
      $byHash[$hash] = $asset
      Copy-Item $_.FullName (Join-Path $Stage $asset) -Force
    }
    $asset = $byHash[$hash]
    $rows += [pscustomobject]@{
      Course = $course; Term = $term; FileName = $_.Name
      Asset = $asset; Url = "$baseUrl/$asset"; Bytes = $_.Length; Hash = $hash
    }
  }
}

$rows | Export-Csv -Path $Manifest -NoTypeInformation -Encoding UTF8
$staged = Get-ChildItem $Stage -Filter *.pdf
"Original files: $($rows.Count)"
"Unique assets staged: $($staged.Count)"
"Staged size: {0:N0} MB" -f (($staged | Measure-Object Length -Sum).Sum/1MB)
"Manifest: $Manifest"
