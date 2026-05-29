# Generate per-course teaching listing pages (courses/<slug>.qmd) from the manifest.
# Each page groups materials by term and links every file to its Release-asset URL.
param(
  [string]$Manifest = "docs\superpowers\migration-notes\teaching-manifest.csv",
  [string]$OutDir   = "courses"
)

$display = @{
  "EcoIV"           = @{ slug="ecoiv";             name="Economía IV" }
  "Microeconometria"= @{ slug="microeconometria";  name="Microeconometría Aplicada / Inferencia Causal" }
  "AnalisisEmpirico"= @{ slug="analisis-empirico"; name="Seminario de Análisis Empírico" }
  "FieldExperiments"= @{ slug="field-experiments"; name="Experimental Methods in Development Research" }
  "TeoJuegos201319" = @{ slug="game-theory-2013";  name="Game Theory (2013)" }
  "TeoJuegos201419" = @{ slug="game-theory-2014";  name="Game Theory (2014)" }
  "MicroII201819"   = @{ slug="micro-ii";          name="Intermediate Microeconomics" }
  "MicroIII201619"  = @{ slug="micro-iii";         name="Advanced Microeconomics" }
}

New-Item -ItemType Directory -Force -Path $OutDir | Out-Null
$rows = Import-Csv $Manifest
# merge Inferencia Causal into Microeconometría Aplicada (one combined course)
foreach ($r in $rows) { if ($r.Course -eq 'Inferencia') { $r.Course = 'Microeconometria' } }
$map = @{}   # course -> slug (for teaching.qmd)

foreach ($cg in ($rows | Group-Object Course)) {
  $course = $cg.Name
  if (-not $display.ContainsKey($course)) { continue }
  $slug = $display[$course].slug
  $name = $display[$course].name
  $map[$course] = $slug

  $sb = New-Object System.Text.StringBuilder
  [void]$sb.AppendLine("---")
  [void]$sb.AppendLine("title: `"$name`"")
  [void]$sb.AppendLine("description: `"Course materials for $name, taught by Mauricio Romero.`"")
  [void]$sb.AppendLine("---")
  [void]$sb.AppendLine("")
  [void]$sb.AppendLine("[← All teaching](../teaching.html)")
  [void]$sb.AppendLine("")

  # group by term, terms with content; sort descending (recent first), blank term last
  $terms = $cg.Group | Group-Object Term | Sort-Object { if ($_.Name) { $_.Name } else { "0" } } -Descending
  foreach ($tg in $terms) {
    if ($tg.Name) { [void]$sb.AppendLine("## $($tg.Name)`n") }
    foreach ($f in ($tg.Group | Sort-Object FileName)) {
      [void]$sb.AppendLine("- [$($f.FileName)]($($f.Url))")
    }
    [void]$sb.AppendLine("")
  }
  Set-Content -Path (Join-Path $OutDir "$slug.qmd") -Value $sb.ToString() -Encoding UTF8
}

# emit the course->slug map for teaching.qmd wiring
$map.GetEnumerator() | Sort-Object Name | ForEach-Object { "$($_.Key) => courses/$($_.Value).html" }
"Generated $($map.Count) course pages in $OutDir/"
