# Recover teaching files that were absent from the FTP download but are still served by the
# live WordPress site. For each PDF_MISSING row in teaching-resolved.csv, fetch its original
# mauricio-romero.com URL; on HTTP 200 save it to the expected public_html\pdfs path so the
# resolver will reclassify it PDF_OK on the next run. Reports what recovered vs is truly gone.
param(
  [string]$Resolved = "docs\superpowers\migration-notes\teaching-resolved.csv",
  [string]$Report   = "docs\superpowers\migration-notes\recover-report.txt",
  [switch]$Upload,
  [string]$Repo = "mauricioromero86/mauricioromero86.github.io",
  [string]$Tag  = "teaching-archive"
)
$ErrorActionPreference = 'Stop'
$rows = Import-Csv $Resolved
$miss = $rows | Where-Object { $_.status -eq 'PDF_MISSING' } |
        Select-Object href, local -Unique
$log = New-Object System.Collections.Generic.List[string]
$recovered = New-Object System.Collections.Generic.List[string]   # local paths to upload
foreach ($m in $miss) {
  $url = $m.href; $local = $m.local
  if (-not $local) { $log.Add("SKIP (no local path)  $url"); continue }
  $dir = Split-Path $local -Parent
  if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Force -Path $dir | Out-Null }
  try {
    $resp = Invoke-WebRequest -Uri $url -OutFile $local -PassThru -TimeoutSec 60
    if ((Test-Path $local) -and ((Get-Item $local).Length -gt 0)) {
      $recovered.Add($local); $log.Add("OK    $([math]::Round((Get-Item $local).Length/1KB)) KB  $url")
    } else { $log.Add("EMPTY $url"); if (Test-Path $local) { Remove-Item $local -Force } }
  } catch {
    $log.Add("GONE  $url")
    if (Test-Path $local) { Remove-Item $local -Force }
  }
}
$header = "Recovered $($recovered.Count) / $($miss.Count) distinct PDF_MISSING files"
Set-Content -Path $Report -Value (@($header,"") + $log) -Encoding utf8
$header

if ($Upload -and $recovered.Count -gt 0) {
  # asset name mirrors resolve-teaching.ps1 AssetName(): flatten the post-/pdfs/ path
  $assets = New-Object System.Collections.Generic.List[string]
  foreach ($lp in $recovered) {
    $rel = ($lp -replace '^.*\\pdfs\\','') # e.g. EcoIV\20231\Temario.pdf
    $asset = ($rel -replace '[\\/ ]','_') -replace '[^A-Za-z0-9._-]','_'
    $stage = Join-Path $env:TEMP $asset
    Copy-Item -LiteralPath $lp -Destination $stage -Force
    $assets.Add($stage)
  }
  & gh release upload $Tag @assets --repo $Repo --clobber
  "Uploaded $($assets.Count) assets to $Tag"
}
