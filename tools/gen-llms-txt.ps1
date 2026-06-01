<#
.SYNOPSIS
  Regenerate the root llms.txt index from research.qmd.

.DESCRIPTION
  Thin wrapper around tools/gen-llms-txt.py. Lists every paper that already has
  a generated <name>.pdf.md twin, pointing LLMs at the Markdown version with the
  PDF noted alongside. Run after convert-paper-md.ps1.

.EXAMPLE
  ./tools/gen-llms-txt.ps1
#>
$ErrorActionPreference = "Stop"
$repo = Split-Path -Parent $PSScriptRoot
python (Join-Path $repo "tools/gen-llms-txt.py")
