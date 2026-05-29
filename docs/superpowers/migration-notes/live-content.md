# Recovered live-site content (T7)

Source: https://mauricio-romero.com (WordPress/Mesmerize), fetched 2026-05-28.
Authoritative for **bio prose, link sets, external data URLs**. Cross-check publication
list against `C:\Users\mauri\Dropbox\CV\CV-ENG.tex`.

## Navigation slugs (preserve via Quarto `aliases`)

| Live URL | New page | alias to add |
|----------|----------|--------------|
| `/` | index.qmd | — |
| `/research/` | research.qmd | `/research/` |
| `/teaching/` | teaching.qmd | `/teaching/` |
| `/data-and-code/` | data-code.qmd | `/data-and-code/` |

## Social / external links

- Email: `mtromero@itam.mx`
- Google Scholar: `https://scholar.google.com.au/citations?user=BD8UfDoAAAAJ&hl=en`
- Twitter/X: `https://twitter.com/marome1`
- Bluesky: `https://bsky.app/profile/marome1.bsky.social`
- CV PDF: `/pdfs/Mauricio-Romero-CV.pdf`

## Headshot

Not a plain `<img>` (Mesmerize CSS background). Not found by scrape. **Action (T13):** locate
in WP media library or request the photo file from the owner.

## Bio (verbatim)

> Associate Professor of Economics at ITAM | Co-Editor at the Journal of Development Economics
>
> I was born and raised in Colombia, where I earned a B.A. in economics (summa cum laude) and a B.A. in mathematics (cum laude) from Universidad de los Andes. I received my Ph.D. in economics from the University of California, San Diego.
>
> I hold affiliations at the Jameel Poverty Action Lab (J-PAL), Innovations for Poverty Action (IPA), Experiments in Governance and Politics (EGAP), the Center for Global Development (CGD), the Bureau for Research and Economic Analysis of Development (BREAD), and the Institute for Labor Economics (IZA).
>
> I am a Jacobs Foundation Research Fellow (2024-2026 cohort) and currently serve on the Executive Committee of LACEA (2024-2027).
>
> My work focuses on the bottlenecks that impede high-quality government provision of education, health care, and environmental protection. In conjunction with my empirical research agenda, I work on methodological issues in applied econometrics and statistics.

## Research page (structure + entries)

Sections, in order: **Publications (Peer-Reviewed)** (15), **Comments, proceedings, and others** (2),
**Non-econ peer-reviewed articles** (2), **Working papers** (2), **Work in progress** (9),
**Policy and popular writing** (9), **Resting papers** (3).

Full entries with titles, coauthors, venues, and link labels are in the fetch log; the list
matches `CV-ENG.tex` (verify titles/coauthors/venues against it). The live page also carries
rich per-paper links (Final Manuscript, AEA RCT registration, NBER WP, Data and code, media).
For migration v1, each entry needs at minimum: title, coauthors, venue+year/status, and the
Journal/DOI link (published) or `/pdfs/papers/<file>.pdf` (working/resting). Richer link sets
can be added incrementally.

Working/resting paper PDFs (preserve `/pdfs/papers/` paths):
- The incidence of affirmative action (R&R RESTud) → `/pdfs/papers/CG_RTE_Draft.pdf`
- Benefit Plans, Insurer Competition… → `/pdfs/papers/Romero_Pharma.pdf`
- Using IV under partial observability… → `/pdfs/papers/partialiv.pdf`

## Teaching page (verbatim structure)

**ITAM:** Economía IV (Fall 2018–Fall 2025); Microeconometría Aplicada (Fall 2020–Fall 2023);
Inferencia Causal (Fall 2025, Spring 2026); Seminario de Análisis Empírico (Spring 2026).
**U. Bern:** Experimental Methods in Development Research (Spring 2020).
**U. de los Andes:** Advanced Microeconomics (2016); Game Theory (2013, 2014); Calculus I (2009).
**U. del Rosario:** Intermediate Microeconomics (2018); Mathematical Economics (2011).
Most ITAM offerings link to materials folders under `/pdfs/` (EcoIV, Microeconometria,
Inferencia, AnalisisEmpirico).

## Data & Code page — EXTERNAL replication URLs (already hosted; survive Bluehost)

- PSL/LEAP — Harvard Dataverse `doi:10.7910/DVN/5OPIYU`; "Beyond Short-term Gains" Zenodo `record/5579799`
- KiuFunza Tanzania — `doi:10.7910/DVN/XAOOTR`; "Designing Teacher Performance Pay" Zenodo `10.5281/zenodo.7411312`
- Communal Property Rights & Deforestation — `doi:10.7910/DVN/YMWIAR`
- Local Incentives & National Tax Evasion — `doi:10.7910/DVN/NML0MG`
- Direct vs Indirect Management Training — `doi:10.7910/DVN/7SDWNS`
- Cross-Age Tutoring (Kenya) — `doi:10.7910/DVN/IGZJ2J`
- Factorial Designs… — `doi:10.7910/DVN/XG6U9H`
- COVID-19 Learning Loss & Recovery (India) — `doi:10.7910/DVN/XGY7CV`

### ⚠ Self-hosted on Bluehost — MUST be rehomed before Bluehost is dropped (owner action)

- **QJE "Inputs, Incentives, and Complementarities" replication** → currently `/replicationData/QJE_Replication.zip` (47 MB). Rehome to Zenodo/Dataverse; relink.
- **SISMED pharmaceutical pricing** CSVs (2006–2016), INVIMA CUM lists, benefit-plan legislation (Acuerdos/Resoluciones 2002–2015) → `/data/sismed/...`
- **Colombia medical providers (IPS)** — Prestadores/Sedes/Servicios/CapacidadInstalada CSV + SedesGeo.zip → `/data/ips/...`
  (`data/` is 586 MB total — not committed to the repo; needs a data-repository home if these links are to survive.)

### Interactive tool to migrate in-repo

- Air-quality (Bogotá) locality reports → `/polucion/*.html` (16 localities). Keep paths.
