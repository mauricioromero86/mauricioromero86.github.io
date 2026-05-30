# Teaching files that could not be migrated

These links appeared on the old WordPress site but their target files were **absent from the
FTP download and now return HTTP 404 on the live site too** (checked 2026-05-30). They are
therefore genuinely lost, not merely unmigrated — the generator (`gen-teaching-pages.ps1`)
drops them automatically because their `Status` in `teaching-resolved.csv` is `PDF_MISSING` or
`NONPDF_MISSING`. If the originals resurface, drop them under `public_html/pdfs/<path>`, run
`tools/recover-missing.ps1 -Upload`, then re-resolve + regenerate and they will reappear.

## PDFs (PDF_MISSING) — 17 distinct, all 404 on mauricio-romero.com

| Course | What | Original path |
|--------|------|---------------|
| EcoIV | Past exam: Primer Parcial Fall 2019 | `/pdfs/EcoIV/PastExams/FirstMidterm/28sept2019.pdf` |
| EcoIV | Spring-2023 syllabus | `/pdfs/EcoIV/20231/Temario.pdf` |
| EcoIV | Lecture 17 annotated, Group 2 (Spring 2021) | `/pdfs/EcoIV/20211/Lecture17_2.pdf` |
| EcoIV | 2022 partial-1 extra solutions (Primavera, Otoño) | `/pdfs/EcoIV/PastExams/FirstMidterm/Solucion_Parcial_1_2022_{Primavera,Otono}_Parte2.pdf` |
| MicroII | Taller 1–5 solutions | `/pdfs/MicroII201819/Taller{1..5}Sol.pdf` |
| MicroII | Taller Parcial 1 | `/pdfs/MicroII201819/TallerParcial1.pdf` |
| MicroII | Quiz 1–4 solutions | `/pdfs/MicroII201819/Quiz{1..4}Sol.pdf` |
| MicroIII | Taller 5 solution | `/pdfs/MicroIII201619/Taller5Sol.pdf` |
| MicroIII | Parcial 2 solution (2010) | `/pdfs/MicroIII201619/2010/parcial2-sol.pdf` |

## Non-PDF source files (NONPDF_MISSING) — LaTeX sources never uploaded

- **Inferencia / Microeconometría** (Fall 2025, Spring 2026): the 12 `Lecture N - *.tex` source
  files for the "native LaTeX file" links — the compiled PDFs are on the site, the `.tex`
  sources were never on the server.
- **Seminario de Análisis Empírico** (Spring 2026): the 6 shared `Lecture N - *.tex` sources
  (same files as Inferencia).

## Known upstream label issues left as-is (cosmetic, original-site errors)

- **EcoIV "Segundo Parcial 2020-Otoño"** in the past-exam bank links the Spring-2021 solution
  `EcoIV_20211_SolucionParcial2.pdf` (mislabeled on the original site); the real Fall-2020
  second midterm is the separate "Segundo Parcial 2020-2" → `..._SecondMidterm_Nov2020.pdf`.
- **MicroII Quiz 4 "Solución"** points to `SolQuiz3.pdf` (the real `SolQuiz4`/`Quiz4Sol` is
  one of the 404s above). Two byte-identical scrape rows make this unsafe to auto-correct;
  left pointing at the original target.
- **MicroII "Taller Parcial 2"** points to a `MicroIII201619` file — a genuine cross-course
  reuse on the original site (same problem set in both courses), kept verbatim.
