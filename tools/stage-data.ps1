# Stage + upload the research datasets (SISMED, IPS, class, replicationData) as assets on a
# GitHub Release ('data-archive'), naming each asset by its original site path so the old
# per-file links can be reconstructed. Emits a manifest: original URL path -> asset -> new URL.
param(
  [string]$Root  = "public_html",
  [string]$Stage = "$env:TEMP\release-data",
  [string]$Manifest = "docs\superpowers\migration-notes\data-manifest.csv",
  [string]$Repo  = "mauricioromero86/mauricioromero86.github.io",
  [string]$Tag   = "data-archive",
  [switch]$Upload
)
$ErrorActionPreference = 'Stop'
$base = "https://github.com/$Repo/releases/download/$Tag"
if (Test-Path $Stage) { Remove-Item $Stage -Recurse -Force }
New-Item -ItemType Directory -Force -Path $Stage | Out-Null

# dirs to publish (relative to $Root); keep the leading folder in the asset name
$dirs = "data\sismed","data\ips","data\class","replicationData"
$rootFull = (Resolve-Path $Root).Path
$rows = @()
foreach ($d in $dirs) {
  $full = Join-Path $Root $d
  if (-not (Test-Path $full)) { continue }
  Get-ChildItem $full -File -Recurse | ForEach-Object {
    $rel = $_.FullName.Substring($rootFull.Length).TrimStart('\')   # data\sismed\2016.csv
    $asset = ($rel -replace '[\\/ ]','_') -replace '[^A-Za-z0-9._-]','_'  # data_sismed_2016.csv
    $origPath = ($rel -replace '\\','/')                            # data/sismed/2016.csv (matches old site path)
    Copy-Item -LiteralPath $_.FullName -Destination (Join-Path $Stage $asset) -Force
    $rows += [pscustomobject]@{ OrigPath=$origPath; Asset=$asset; Url="$base/$asset";
      Bytes=$_.Length; Name=$_.Name }
  }
}
$rows | Export-Csv -Path $Manifest -NoTypeInformation -Encoding UTF8
$staged = Get-ChildItem $Stage -File
"Staged $($staged.Count) files, {0:N1} MB" -f (($staged | Measure-Object Length -Sum).Sum/1MB)
"Manifest: $Manifest"

if ($Upload) {
  # ensure the release exists (gh writes to stderr when missing; don't let that abort)
  $exists = $null
  try { $exists = & gh release view $Tag --repo $Repo 2>$null } catch { $exists = $null }
  if (-not $exists) {
    gh release create $Tag --repo $Repo --title "Research data archive" `
      --notes "Datasets from Mauricio Romero's research: SISMED pharmaceutical pricing (Colombia, 2006-2016), INVIMA drug registries, benefit-plan legislation, IPS medical-provider directory, and replication packages. Mirrors the files formerly hosted at mauricio-romero.com/data and /replicationData."
    "Created release $Tag"
  }
  $files = $staged | ForEach-Object { $_.FullName }
  for ($i=0; $i -lt $files.Count; $i += 20) {
    $chunk = $files[$i..([Math]::Min($i+19,$files.Count-1))]
    gh release upload $Tag @chunk --repo $Repo --clobber
    "  uploaded $([Math]::Min($i+20,$files.Count))/$($files.Count)"
  }
  "Upload complete."
}
