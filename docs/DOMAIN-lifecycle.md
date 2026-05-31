# Domain lifecycle runbook — `mauricio-romero.com`

How to keep, move, or retire the custom domain. This is **contingency planning, not a deadline**:
the domain is prepaid for years. Read the snapshot, then the playbook that matches your decision.

---

## 1. Status snapshot (as of 2026-05)

| Field | Value |
|-------|-------|
| Domain | `mauricio-romero.com` |
| Registrar | **Bluehost Inc.** |
| Created | 2018-05-21 |
| **Paid through** | **2031-05-21** (≈6 years of runway) |
| Lock status | `client transfer prohibited` (normal owner-toggleable lock) |
| Site host | GitHub Pages (`mauricioromero86/mauricioromero86.github.io`) |
| Free fallback URL | `https://mauricioromero86.github.io` (always works, no domain needed) |

**Registration ≠ hosting.** The domain *name* is registered at Bluehost; the *website* is on
GitHub Pages. You are decommissioning Bluehost **hosting** — that does not require giving up the
domain. They are billed and managed separately.

> ⚠️ **The one rule at decommission time:** when you cancel Bluehost **hosting**, do **not**
> cancel the **domain registration**. Before touching the Bluehost account, confirm: (a) domain
> auto-renew is ON, (b) the billing card on file is valid, (c) the account email is one you still
> read. Losing the domain to an expired card is the most common self-inflicted failure here.

**Domain-independent assets:** the `data-archive` and `teaching-archive` GitHub Releases live on
`github.com` and are unaffected by any domain decision — they never break.

---

## 2. Decision tree

- **Keep using the domain** → Playbook A (do nothing but stay paid up).
- **Keep the domain but stop depending on Bluehost** → Playbook B *(recommended hygiene).*
- **Stop paying / let it go** → Playbook C (fall back to the free github.io URL).

Trigger to revisit: an annual renewal charge you no longer want to pay, or Bluehost account
closure. Given that paper PDFs are cited by their `mauricio-romero.com/pdfs/papers/...` URLs,
**the default recommendation is to keep the domain (A or B), not drop it (C).**

---

## 3. Playbook A — Keep the domain (status quo)

1. Ensure **auto-renew is ON** in the Bluehost domain dashboard; keep a valid card on file.
2. Set a **calendar reminder for ~April each year** to confirm the renewal went through.
3. Repo side stays exactly as configured at cutover:
   - `CNAME` file = `mauricio-romero.com` (re-added during the DNS cutover; see project tasks
     T19–T21).
   - DNS at the registrar: four A records for `@` → `185.199.108.153`, `185.199.109.153`,
     `185.199.110.153`, `185.199.111.153`; `www` CNAME → `mauricioromero86.github.io`.
4. Nothing in the repo changes for a renewal. Done.

---

## 4. Playbook B — Decouple the registrar from Bluehost (recommended, keeps the domain)

**Why:** removes the last tie to the host you're leaving, and renewals are usually cheaper
elsewhere. You keep the domain and the site is unaffected.

### Registrar options (the "advise me")

| Registrar | ~Renewal /yr (.com) | DNS | Trade-off |
|-----------|--------------------|-----|-----------|
| **Cloudflare Registrar** | ~$10–11 (at cost, zero markup) | **Must** use Cloudflare DNS | Cheapest long-term; one-time nameserver move. Best if you want lowest cost forever. |
| **Porkbun** / **Namecheap** | ~$10–12 | Registrar-provided DNS (or any) | Simplest mental model; keep DNS where the registrar puts it. Good middle ground. |
| **Stay at Bluehost (domain-only)** | ~$18–21 | Bluehost DNS | Simplest now, but pricier and keeps a Bluehost tie. **Not recommended long-term.** |

**Recommendation:** Cloudflare Registrar if you're comfortable moving nameservers (best price +
clean DNS UI); Porkbun if you want the least fuss. Either fully decouples you from Bluehost.

### Transfer mechanics (do this **while the Bluehost account is still active**)

1. In Bluehost: **unlock** the domain (clear `client transfer prohibited`) and **request the
   EPP / auth code**. Confirm the domain is **>60 days** past its creation/last transfer (it is).
2. At the new registrar: start an inbound transfer, paste the auth code, pay (a transfer normally
   **adds one year** to the expiry — you don't lose the prepaid time).
3. Approve the transfer email; it completes in a few days.
4. Re-create DNS at the new registrar: the **four A records** + **`www` CNAME** from Playbook A
   (and, if Cloudflare, set the GitHub Pages records there).
5. Verify `https://mauricio-romero.com` still serves the site and HTTPS is valid.
6. Only **after** the transfer is confirmed, cancel Bluehost hosting.

No repo changes needed — `site-url` and `CNAME` stay `mauricio-romero.com`.

---

## 5. Playbook C — Drop the domain (fall back to `mauricioromero86.github.io`)

A ~15-minute repo change whenever you decide. Either let the registration lapse or actively
revert. The site keeps working at the free github.io URL.

### Exact repo edits (every spot the absolute host appears)

1. `_quarto.yml:15` — `site-url:` → `"https://mauricioromero86.github.io"`
2. `_quarto.yml:16` — `image:` (OG fallback) → `"https://mauricioromero86.github.io/img/headshot.jpg"`
3. `_includes/person-jsonld.html` — lines 12 (`image`) and 14 (`url`): swap host.
4. `_includes/website-jsonld.html` — lines 7 and 12 (`url`): swap host.
5. `filters/seo-meta.lua:6` — `local SITE_URL = "https://mauricioromero86.github.io"`
   *(this filter hardcodes the host independently of `site-url` — easy to miss).*
6. Delete the `CNAME` file from the repo **and** clear the custom domain in GitHub repo
   **Settings → Pages**.
7. `quarto render` → `sitemap.xml`, the `robots.txt` sitemap line, and canonical/OG tags
   regenerate to the new host automatically (they derive from `site-url` + the filter).

To re-verify nothing was missed:
`grep -rn "mauricio-romero\.com" _quarto.yml _includes/ filters/` should return **nothing**.

### Cost of dropping — read before choosing C

Every external citation and CV link of the form `mauricio-romero.com/pdfs/papers/<file>.pdf` will
**404**. GitHub Pages has **no server-side 301s**, and once the apex domain stops resolving there's
nothing to redirect. Mitigations:

- **(a)** Before lapsing, change the CV's link base to `mauricioromero86.github.io` for all future
  copies. Already-printed/indexed citations still break.
- **(b)** If redirects are essential, keep the domain one more cycle pointed at a cheap redirect
  service (e.g. Cloudflare bulk redirect) `mauricio-romero.com/* → mauricioromero86.github.io/*`.
  This costs roughly the same as just keeping the domain — which is why **B is usually better than C.**

---

## 6. Quick reference

| Action | Where | Cost/yr | Reversible? |
|--------|-------|---------|-------------|
| Keep as-is (A) | Bluehost auto-renew | ~$18–21 | n/a |
| Transfer registrar (B) | New registrar + DNS | ~$10–12 | Yes (transfer again) |
| Drop, fall back to github.io (C) | 5 repo files + Pages settings | $0 | Yes *until* the name is re-registered by someone else |
| Release assets (data/teaching) | `github.com` | $0 | Unaffected by any choice |

**Bottom line:** the domain is safe until 2031. When a renewal decision comes, prefer **B**
(cheap, decoupled, keeps every citation link working). Only choose **C** if you accept that cited
paper URLs will break.
