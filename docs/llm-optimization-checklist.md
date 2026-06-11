# LLM-Optimization — Owner Action Checklist

Off-repo actions that complete the site's LLM/AI-discoverability work
(repo-side work: ScholarlyArticle JSON-LD, `@id` entity graph, RePEc/OpenAlex
`sameAs`, `llms.txt` + `.pdf.md` twins — all done in-repo). Check items off as
completed.

## One-time setup

- [ ] **Bing Webmaster Tools** — <https://www.bing.com/webmasters>. Verify
  `mauricio-romero.com` (fastest: "Import from Google Search Console"), then
  submit `https://mauricio-romero.com/sitemap.xml`. ChatGPT's web search is
  Bing-backed, so Bing indexing directly affects ChatGPT citations.
  Optionally enable **IndexNow** for instant recrawl pings.
- [ ] **GA4 channel group for LLM referrals** — GA4 Admin → Data display →
  Channel groups → create custom channel **"LLM Referrals"** with condition
  *Source matches regex*:
  `chatgpt\.com|chat\.openai\.com|perplexity\.ai|claude\.ai|gemini\.google\.com|copilot\.microsoft\.com`
  Lets you track what share of visits come from AI assistants.
- [x] **Wikidata item** — created 2026-06-11:
  [Q140170702](https://www.wikidata.org/wiki/Q140170702) (verified: ORCID
  P496, Scholar P1960 `BD8UfDoAAAAJ`, employer ITAM P108, website P856,
  RePEc P2428 `pro605`). Added to the `sameAs` arrays in
  `_includes/person-jsonld.html`, `_includes/website-jsonld.html`, and the
  research-page Person node (`tools/gen-research-jsonld.py`).
- [ ] **Validate structured data post-deploy** — paste
  `https://mauricio-romero.com/research.html` and the homepage into
  <https://validator.schema.org> and Google's Rich Results Test; expect
  ScholarlyArticle ×21 + Person/ProfilePage with no errors.

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
