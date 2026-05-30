# Resolve every original teaching link (teaching-links.tsv) to a deployable URL.
# PDFs -> existing Release asset (via teaching-manifest.csv, dedup-by-hash).
# Non-PDFs (.R/.csv/.tex/...) -> Release asset named by original path (to be uploaded).
# External (uniandes) -> kept as-is. Emits a resolved CSV + a human report.
param(
  [string]$Tsv      = "docs\superpowers\migration-notes\teaching-links.tsv",
  [string]$Manifest = "docs\superpowers\migration-notes\teaching-manifest.csv",
  [string]$OutCsv   = "docs\superpowers\migration-notes\teaching-resolved.csv",
  [string]$Report   = "docs\superpowers\migration-notes\teaching-resolve-report.txt",
  [string]$Repo     = "mauricioromero86/mauricioromero86.github.io",
  [string]$Tag      = "teaching-archive",
  [string]$Src      = "public_html\pdfs"
)
$ErrorActionPreference = 'Stop'
$base = "https://github.com/$Repo/releases/download/$Tag"

function Sanitize([string]$rel) { ($rel -replace '[\\/ ]','_') -replace '[^A-Za-z0-9._-]','_' }

# manifest: (Course|Term|FileName) -> asset Url  (first wins)
$mUrl = @{}
foreach ($r in (Import-Csv $Manifest)) {
  $k = "$($r.Course)|$($r.Term)|$($r.FileName)"
  if (-not $mUrl.ContainsKey($k)) { $mUrl[$k] = $r.Url }
}

$rows = @()
$lines = Get-Content $Tsv -Encoding UTF8
for ($i=1; $i -lt $lines.Count; $i++) {
  $p = $lines[$i] -split "`t"
  if ($p.Count -lt 5) { continue }
  $course=$p[0]; $term=$p[1]; $section=$p[2]; $label=$p[3]; $href=$p[4]
  $status=''; $url=''; $asset=''; $local=''
  if ($href -match 'economia\.uniandes\.edu\.co') {
    $status='EXTERNAL'; $url=$href
  } elseif ($href -match 'mauricio-romero\.com/(.+)$') {
    $rel = [uri]::UnescapeDataString($Matches[1])          # e.g. pdfs/EcoIV/20191/Lecture1.pdf
    $relp = $rel -replace '^pdfs/',''                       # EcoIV/20191/Lecture1.pdf
    $parts = $relp -split '/'
    $fname = $parts[-1]
    $pcourse = $parts[0]
    $pterm = if ($parts.Count -ge 3) { $parts[1] } else { '' }
    $local = Join-Path $Src ($relp -replace '/','\')
    $exists = Test-Path -LiteralPath $local
    if ($fname -match '\.pdf$') {
      $k = "$pcourse|$pterm|$fname"
      if ($mUrl.ContainsKey($k)) { $status='PDF_OK'; $url=$mUrl[$k] }
      elseif ($exists) { $status='PDF_UNMAPPED'; $asset=Sanitize($relp); $url="$base/$asset" }
      else { $status='PDF_MISSING'; $asset=Sanitize($relp); $url="$base/$asset" }
    } else {
      if ($exists) { $status='NONPDF_OK'; $asset=Sanitize($relp); $url="$base/$asset" }
      else { $status='NONPDF_MISSING'; $asset=Sanitize($relp); $url="$base/$asset" }
    }
  } else { $status='OTHER'; $url=$href }
  $rows += [pscustomobject]@{ Course=$course; Term=$term; Section=$section; Label=$label;
    Href=$href; Status=$status; Url=$url; Asset=$asset; Local=$local }
}
$rows | Export-Csv -Path $OutCsv -NoTypeInformation -Encoding UTF8

# report
$sb = New-Object System.Text.StringBuilder
[void]$sb.AppendLine("### STATUS COUNTS ###")
foreach ($g in ($rows | Group-Object Status | Sort-Object Name)) { [void]$sb.AppendLine(("{0,-16} {1}" -f $g.Name,$g.Count)) }
[void]$sb.AppendLine("")
[void]$sb.AppendLine("### NON-PDF / UNMAPPED files to UPLOAD (exist locally) ###")
foreach ($r in ($rows | Where-Object { $_.Status -in 'NONPDF_OK','PDF_UNMAPPED' } | Sort-Object Asset -Unique)) {
  [void]$sb.AppendLine("$($r.Asset)`t<= $($r.Local)")
}
[void]$sb.AppendLine("")
[void]$sb.AppendLine("### MISSING (no local file; link will be dropped) ###")
foreach ($r in ($rows | Where-Object { $_.Status -like '*MISSING*' } | Sort-Object Href -Unique)) {
  [void]$sb.AppendLine("$($r.Status)`t$($r.Href)")
}
[IO.File]::WriteAllText((Resolve-Path -LiteralPath '.').Path + "\$Report", $sb.ToString(), (New-Object Text.UTF8Encoding $false))
"resolved rows: $($rows.Count); wrote $OutCsv and $Report"
