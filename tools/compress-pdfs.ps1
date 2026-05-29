# Compress PDFs from $Src into $Dst (preserving relative paths) using Ghostscript /ebook.
# Keeps whichever of compressed/original is smaller. Reports before/after totals.
param(
  [Parameter(Mandatory=$true)][string]$Src,
  [Parameter(Mandatory=$true)][string]$Dst
)

# Locate a Ghostscript console executable
$gs = @(
  (Get-ChildItem "$env:ProgramFiles\gs\*\bin\gswin64c.exe" -ErrorAction SilentlyContinue),
  (Get-ChildItem "$env:ProgramFiles\QGIS*\bin\gswin64c.exe"  -ErrorAction SilentlyContinue)
) | ForEach-Object { $_ } | Select-Object -First 1 -ExpandProperty FullName
if (-not $gs) { throw "Ghostscript (gswin64c.exe) not found." }

$srcRoot = (Resolve-Path $Src).Path
$before = 0.0; $after = 0.0; $n = 0
Get-ChildItem -Path $Src -Recurse -Filter *.pdf | ForEach-Object {
  $rel = $_.FullName.Substring($srcRoot.Length).TrimStart('\')
  $out = Join-Path $Dst $rel
  New-Item -ItemType Directory -Force -Path (Split-Path $out) | Out-Null
  # PS 5.1 mangles `-sOutputFile=<path>` when passed via the call operator, so use
  # Start-Process with an explicit argument array (each element passed verbatim).
  $gsArgs = @("-q","-sDEVICE=pdfwrite","-dCompatibilityLevel=1.4","-dPDFSETTINGS=/ebook",
              "-dNOPAUSE","-dBATCH","-sOutputFile=$out",$_.FullName)
  Start-Process -FilePath $gs -ArgumentList $gsArgs -Wait -NoNewWindow | Out-Null
  if ((-not (Test-Path $out)) -or ((Get-Item $out).Length -ge $_.Length)) {
    Copy-Item $_.FullName $out -Force   # keep original if compression failed or inflated
  }
  $before += $_.Length; $after += (Get-Item $out).Length; $n++
}
"Files: $n"
"Before: {0:N1} MB" -f ($before/1MB)
"After:  {0:N1} MB" -f ($after/1MB)
if ($before -gt 0) { "Reduction: {0:N1}%" -f (100*(1-($after/$before))) }
