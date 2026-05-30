# Stage the non-PDF teaching files (.R/.csv/.tex/.png/.html/.docx) that exist locally and
# upload them to the teaching-archive Release under their original-path asset names.
param(
  [string]$Resolved = "docs\superpowers\migration-notes\teaching-resolved.csv",
  [string]$Stage    = "$env:TEMP\release-teaching-nonpdf",
  [string]$Repo     = "mauricioromero86/mauricioromero86.github.io",
  [string]$Tag      = "teaching-archive",
  [switch]$Upload
)
$ErrorActionPreference = 'Stop'
if (Test-Path $Stage) { Remove-Item $Stage -Recurse -Force }
New-Item -ItemType Directory -Force -Path $Stage | Out-Null

$rows = Import-Csv $Resolved | Where-Object { $_.Status -in 'NONPDF_OK','PDF_UNMAPPED' }
$seen = @{}
$n = 0
foreach ($r in $rows) {
  if ($seen.ContainsKey($r.Asset)) { continue }
  $seen[$r.Asset] = $true
  if (Test-Path -LiteralPath $r.Local) {
    Copy-Item -LiteralPath $r.Local -Destination (Join-Path $Stage $r.Asset) -Force
    $n++
  }
}
"Staged $n unique non-PDF files to $Stage"

if ($Upload) {
  $files = Get-ChildItem $Stage | ForEach-Object { $_.FullName }
  "Uploading $($files.Count) assets to $Repo @ $Tag ..."
  # upload in chunks of 40 to keep the command line sane
  for ($i=0; $i -lt $files.Count; $i += 40) {
    $chunk = $files[$i..([Math]::Min($i+39,$files.Count-1))]
    gh release upload $Tag @chunk --repo $Repo --clobber
    "  uploaded $([Math]::Min($i+40,$files.Count))/$($files.Count)"
  }
  "Upload complete."
}
