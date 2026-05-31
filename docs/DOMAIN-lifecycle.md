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

> **Chosen path: Playbook B → Cloudflare Registrar.** Transfer the domain off Bluehost to
> Cloudflare (~$10/yr, at cost) so it's decoupled from the host being decommissioned. **Do the
> transfer before cancelling Bluehost hosting** — you need the Bluehost account active to get the
> transfer auth code.

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

## 4. Playbook B — Transfer to Cloudflare Registrar (CHOSEN PATH, keeps the domain)

**Why:** removes the last tie to Bluehost (the host being shut down) and drops the renewal to
~$10/yr at cost. You keep the domain; the site is unaffected; all citation links keep working.

> **Cloudflare wrinkle:** Cloudflare Registrar only registers domains whose **DNS is already on
> Cloudflare**. So the order is *add to Cloudflare DNS first → then transfer the registration*,
> not the other way around. Steps below are in the correct order.

### Registrar options considered (for the record)

| Registrar | ~Renewal /yr (.com) | DNS | Note |
|-----------|--------------------|-----|------|
| **Cloudflare Registrar** ← chosen | ~$10–11 (at cost, zero markup) | **Must** use Cloudflare DNS | Cheapest long-term; one-time nameserver move. |
| Porkbun / Namecheap | ~$10–12 | Registrar-provided DNS | Simpler (no nameserver move), slightly pricier. |
| Stay at Bluehost (domain-only) | ~$18–21 | Bluehost DNS | Keeps a Bluehost tie; not recommended. |

### Step-by-step (do all of this **while the Bluehost account is still active**)

**Phase 1 — Move DNS to Cloudflare (no registration change yet; site keeps working):**

1. Create a free **Cloudflare** account → **Add a site** → `mauricio-romero.com`. Cloudflare scans
   existing DNS and assigns you **two Cloudflare nameservers** (e.g. `xxx.ns.cloudflare.com`).
2. In Cloudflare DNS, set the **GitHub Pages records** (these are the cutover records — same as
   Playbook A):
   - `A  @  185.199.108.153`
   - `A  @  185.199.109.153`
   - `A  @  185.199.110.153`
   - `A  @  185.199.111.153`
   - `CNAME  www  mauricioromero86.github.io`
   - **Set each record's proxy status to "DNS only" (grey cloud), NOT proxied (orange).**
     GitHub Pages provisions its own HTTPS cert; Cloudflare's proxy interferes with that. Grey
     cloud = Cloudflare is just authoritative DNS, traffic goes straight to GitHub.
3. In **Bluehost**, change the domain's **nameservers** to the two Cloudflare nameservers from
   step 1. Wait for propagation (minutes to a few hours). The site keeps resolving throughout.

**Phase 2 — Transfer the registration to Cloudflare:**

4. In **Bluehost**: **unlock** the domain (clear `client transfer prohibited`) and **request the
   EPP / auth code**. (Domain is well past the 60-day post-creation window, so it's eligible.)
5. In **Cloudflare → Registrar → Transfer Domains**: select `mauricio-romero.com`, paste the auth
   code, pay. A transfer **adds one year** to the expiry — you don't lose prepaid time.
6. **Approve the confirmation email** (sent to the domain's registrant address). Completes in up to
   ~5 days; Bluehost may let you "accept" it to speed it up.

**Phase 3 — Finish the site cutover + retire Bluehost:**

7. Tell Claude the domain is live on Cloudflare → Claude re-adds the `CNAME` file
   (`mauricio-romero.com`) to the repo and enables **Enforce HTTPS** in GitHub Pages settings once
   the cert provisions (can take a few hours after DNS resolves).
8. Verify `https://mauricio-romero.com` and `https://www.mauricio-romero.com` both serve the site
   with a valid cert; spot-check a paper PDF link.
9. Submit `https://mauricio-romero.com/sitemap.xml` to Google Search Console.
10. **Only now** cancel Bluehost **hosting** — the domain already lives at Cloudflare, so nothing
    is at risk.

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
