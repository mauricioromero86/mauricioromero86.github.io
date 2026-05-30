# Generate per-course teaching pages (courses/<slug>.qmd) from the RESOLVED link map,
# faithfully reproducing the original site: term -> section -> verbatim labels, recent-first.
# Source of truth: teaching-resolved.csv (built by resolve-teaching.ps1 from teaching-links.tsv).
param(
  [string]$Resolved = "docs\superpowers\migration-notes\teaching-resolved.csv",
  [string]$OutDir   = "courses"
)
$ErrorActionPreference = 'Stop'

# Course -> page slug + display name. Inferencia is merged into Microeconometria.
$display = @{
  "EcoIV"            = @{ slug="ecoiv";             name="Economía IV" }
  "Microeconometria" = @{ slug="microeconometria";  name="Microeconometría Aplicada / Inferencia Causal" }
  "AnalisisEmpirico" = @{ slug="analisis-empirico"; name="Seminario de Análisis Empírico" }
  "FieldExperiments" = @{ slug="field-experiments"; name="Experimental Methods in Development Research" }
  "MicroIII"         = @{ slug="micro-iii";         name="Advanced Microeconomics" }
  "MicroII"          = @{ slug="micro-ii";          name="Intermediate Microeconomics" }
  "TeoJuegos"        = @{ slug="game-theory";       name="Game Theory" }
}

# Sections that repeat across terms (past-exam banks): emit ONCE at the page bottom as the
# union across all terms (deduped by URL, recent-term label wins), instead of per term.
$sharedSections = @{
  "EcoIV"     = @('Exámenes viejos de Eco-IV')
  "TeoJuegos" = @('Parciales Viejos y otros materiales de estudio')
  "MicroIII"  = @('Parciales Viejos y otros materiales de estudio')
}

function FriendlyTerm([string]$course,[string]$term) {
  if ($term -match '^(\d{4})-1$') { return "Spring $($Matches[1])" }
  if ($term -match '^(\d{4})-2$') { return "Fall $($Matches[1])" }
  if ($term -match '^(Spring|Summer|Fall|Winter)\s+\d{4}$') { return $term }
  switch -regex ("$course|$term") {
    'TeoJuegos\|2013' { return 'Summer 2013' }
    'TeoJuegos\|2014' { return 'Summer 2014' }
    'MicroII\|2018'   { return 'Summer 2018' }
    'MicroIII\|2016'  { return 'Summer 2016' }
  }
  return $term
}
function TermKey([string]$friendly) {
  if ($friendly -match '(Spring|Summer|Fall|Winter)\s+(\d{4})') {
    $y = [int]$Matches[2]
    $s = @{ Spring=1; Summer=2; Fall=3; Winter=4 }[$Matches[1]]
    return $y*10 + $s
  }
  return 0
}

New-Item -ItemType Directory -Force -Path $OutDir | Out-Null
$rows = Import-Csv $Resolved -Encoding UTF8
foreach ($r in $rows) { if ($r.Course -eq 'Inferencia') { $r.Course = 'Microeconometria' } }
# only rows whose target actually resolves (drop missing files; keep external + hosted)
$rows = $rows | Where-Object { $_.Status -in 'PDF_OK','NONPDF_OK','PDF_UNMAPPED','EXTERNAL' }

$generated = @()
foreach ($course in $display.Keys) {
  $cr = $rows | Where-Object { $_.Course -eq $course }
  if (-not $cr) { continue }
  $slug = $display[$course].slug
  $name = $display[$course].name

  # ordered term list (recent first); keep original row order within term/section
  $termNames = $cr | Select-Object -ExpandProperty Term -Unique
  $terms = $termNames | Sort-Object { TermKey (FriendlyTerm $course $_) } -Descending

  $sb = New-Object System.Text.StringBuilder
  [void]$sb.AppendLine("---")
  [void]$sb.AppendLine("title: `"$name`"")
  [void]$sb.AppendLine("description: `"Course materials for $name, taught by Mauricio Romero.`"")
  [void]$sb.AppendLine("toc: true")
  [void]$sb.AppendLine("toc-location: right")
  [void]$sb.AppendLine("toc-depth: 3")
  [void]$sb.AppendLine("---")
  [void]$sb.AppendLine("")
  [void]$sb.AppendLine("[← All teaching](../teaching.html)")
  [void]$sb.AppendLine("")

  $shared = @(); if ($sharedSections.ContainsKey($course)) { $shared = $sharedSections[$course] }
  # accumulate shared-section rows across all terms (recent-first), deduped by URL
  $sharedRows = [ordered]@{}   # section -> ordered map url -> item
  foreach ($s in $shared) { $sharedRows[$s] = [ordered]@{} }

  foreach ($term in $terms) {
    $tr = $cr | Where-Object { $_.Term -eq $term }
    $friendly = FriendlyTerm $course $term
    # sections in first-seen order
    $secOrder = @(); $seen = @{}
    foreach ($x in $tr) { $s = $x.Section; if (-not $seen.ContainsKey($s)) { $seen[$s]=$true; $secOrder += $s } }
    # non-shared sections for this term (so we don't print an empty term header)
    $termSecs = $secOrder | Where-Object { $shared -notcontains $_ }

    if ($termSecs.Count -gt 0) {
      [void]$sb.AppendLine("## $friendly")
      [void]$sb.AppendLine("")
      foreach ($sec in $termSecs) {
        if ($sec) { [void]$sb.AppendLine("### $sec"); [void]$sb.AppendLine("") }
        foreach ($it in ($tr | Where-Object { $_.Section -eq $sec })) {
          $label = $it.Label -replace '\]','\]'   # escape ] in label
          [void]$sb.AppendLine("- [$label]($($it.Url))")
        }
        [void]$sb.AppendLine("")
      }
    }
    # stash shared-section rows (dedupe by URL; first occurrence = most-recent term wins)
    foreach ($sec in ($secOrder | Where-Object { $shared -contains $_ })) {
      foreach ($it in ($tr | Where-Object { $_.Section -eq $sec })) {
        if (-not $sharedRows[$sec].Contains($it.Url)) { $sharedRows[$sec][$it.Url] = $it }
      }
    }
  }

  # emit each shared section ONCE at the page bottom, as a top-level (##) section
  foreach ($sec in $shared) {
    $items = $sharedRows[$sec].Values
    if (-not $items -or @($items).Count -eq 0) { continue }
    [void]$sb.AppendLine("## $sec")
    [void]$sb.AppendLine("")
    foreach ($it in $items) {
      $label = $it.Label -replace '\]','\]'
      [void]$sb.AppendLine("- [$label]($($it.Url))")
    }
    [void]$sb.AppendLine("")
  }

  $path = Join-Path $OutDir "$slug.qmd"
  [IO.File]::WriteAllText((Resolve-Path '.').Path + "\$path", $sb.ToString(), (New-Object Text.UTF8Encoding $false))
  $generated += "$course -> courses/$slug.qmd ($($cr.Count) links, $($terms.Count) terms)"
}

# clean up obsolete split game-theory pages (replaced by single game-theory.qmd)
foreach ($old in 'game-theory-2013','game-theory-2014') {
  $p = Join-Path $OutDir "$old.qmd"; if (Test-Path $p) { Remove-Item $p -Force; "removed obsolete $p" }
}

$generated
"Generated $($generated.Count) course pages in $OutDir/"
