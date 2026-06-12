# LLM-Optimization — Owner Action Checklist

Off-repo actions that complete the site's LLM/AI-discoverability work
(repo-side work: ScholarlyArticle JSON-LD, `@id` entity graph, RePEc/OpenAlex
`sameAs`, `llms.txt` + `.pdf.md` twins — all done in-repo). Check items off as
completed.

## One-time setup

- [x] **Bing Webmaster Tools** — done 2026-06-12: site verified, sitemap
  submitted. (ChatGPT's web search is Bing-backed, so Bing indexing directly
  affects ChatGPT citations.)
- [x] **GA4 channel group for LLM referrals** — done 2026-06-12: custom
  channel **"LLM Referrals"** with *Source matches regex*
  `chatgpt\.com|chat\.openai\.com|perplexity\.ai|claude\.ai|gemini\.google\.com|copilot\.microsoft\.com`.
  Review its share of traffic in the periodic checks below.
- [x] **Wikidata item** — created 2026-06-11:
  [Q140170702](https://www.wikidata.org/wiki/Q140170702) (verified: ORCID
  P496, Scholar P1960 `BD8UfDoAAAAJ`, employer ITAM P108, website P856,
  RePEc P2428 `pro605`). Added to the `sameAs` arrays in
  `_includes/person-jsonld.html`, `_includes/website-jsonld.html`, and the
  research-page Person node (`tools/gen-research-jsonld.py`).
- [x] **Validate structured data post-deploy** — done 2026-06-12 via
  <https://validator.schema.org> / Google Rich Results Test on the homepage
  and `research.html` (ScholarlyArticle ×21 + Person/ProfilePage). Re-check
  after the next paper is added.

## Periodic (monthly-ish)

- [ ] Ask ChatGPT, Claude, Perplexity, and Gemini: "Who is Mauricio Romero
  (ITAM)?", "What did Romero, Sandefur, and Sandholtz find about outsourcing
  education in Liberia?" — check facts and whether answers cite
  `mauricio-romero.com`. Fix errors at the source (CV/site), the models
  re-crawl.
- [ ] GA4: review the "LLM Referrals" channel share.
- [ ] After each new paper: the `add-publication` skill regenerates
  `llms.txt` + `research-jsonld.html`; re-submit the sitemap in Bing/Google
  if you want a faster recrawl.
