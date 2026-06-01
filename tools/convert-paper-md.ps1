<#
.SYNOPSIS
  Convert a paper PDF (or the whole corpus) to a machine-readable Markdown twin.

.DESCRIPTION
  Thin wrapper around tools/pdf-to-md.py (the actual logic). Produces
  pdfs/papers/<name>.pdf.md with YAML front matter + full text, for LLMs.
  See docs in pdf-to-md.py. Image extraction is disabled by design.

  For the highest-quality LLM refinement pass, set an API key first, e.g.:
    $env:GEMINI_API_KEY = "..."     # then add -UseLlm

.EXAMPLE
  ./tools/convert-paper-md.ps1 aer.20181478.pdf
.EXAMPLE
  ./tools/convert-paper-md.ps1 -All -UseLlm
.EXAMPLE
  ./tools/convert-paper-md.ps1 -All -Jobs 3    # batch mode, 3 workers, models load once
.EXAMPLE
  ./tools/convert-paper-md.ps1 GTO_Learning_Loss.pdf -Engine pandoc -Tex "C:\Users\mauri\Dropbox\Research\GTO_LearningLoss\LaTeX\maintext.tex"
#>
param(
    [Parameter(Position = 0)] [string] $Pdf,
    [switch] $All,
    [ValidateSet("marker", "pandoc")] [string] $Engine = "marker",
    [switch] $UseLlm,
    [string] $Tex,
    [int] $Jobs = 1,
    [switch] $Force
)

$ErrorActionPreference = "Stop"
$repo = Split-Path -Parent $PSScriptRoot
$script = Join-Path $repo "tools/pdf-to-md.py"

$pyArgs = @($script)
if ($All)   { $pyArgs += "--all" }
elseif ($Pdf) { $pyArgs += $Pdf }
$pyArgs += @("--engine", $Engine)
if ($UseLlm) { $pyArgs += "--use-llm" }
if ($Tex)    { $pyArgs += @("--tex", $Tex) }
if ($Jobs -gt 1) { $pyArgs += @("--jobs", $Jobs) }
if ($Force)  { $pyArgs += "--force" }

python @pyArgs
