# idrpros.com

IDR Pros ("Maximizing what you're owed"), serviced by Smith Law:
Dan Smith, Esq., Tampa. Audience: Florida out-of-network providers, physician
groups, and hospital systems. Content is adapted from Dan's newsletter,
"IDR Is Just the Beginning: How Florida Law Recovers What IDR Cannot."

Static single-page site. No build step. No dependencies. No server.

## Files

- `index.html`: the entire site (markup, CSS, JS inline)
- `thanks/index.html`: form confirmation page (used when JS is off)
- `es/`: Spanish page and `es/gracias/` thank-you page (see below)
- `tools/make_es.py`: builds `es/index.html` from `index.html`
- `fonts/`: self-hosted Newsreader, IBM Plex Sans, IBM Plex Mono (woff2)
- `img/idrpros-logo-hero.webp` / `.png`: full logo, transparent, shown large at the top of the page
- `img/og.png`: 1200×630 social share card
- `img/idrpros-logo-white.png`: same, all white, for the navy footer
- `img/idrpros-lockup.png`: icon + "IDR PROS" only, for the header and thanks page
- `img/idrpros-icon.png`: icon mark only
- `favicon.png`, `favicon.ico`, `apple-touch-icon.png`: from the icon mark
- `netlify.toml`: publish settings and security headers
- `_redirects`: www.idrpros.com 301s to idrpros.com
- `robots.txt`, `sitemap.xml`

## Deploy (Netlify)

1. app.netlify.com -> Add new site -> Import an existing project -> GitHub ->
   `garysafirlaw/idrpros`
   - Branch: `main`
   - Build command: (none)
   - Publish directory: `.`
2. Review on the generated `*.netlify.app` URL.
3. **Forms:** Site configuration -> Forms -> enable form detection, then
   redeploy once so Netlify registers the `claims-review` form.
   Forms -> Form notifications -> Add notification -> Email ->
   Dan's real inbox (and anyone else who should get leads).
   Submit one test entry from the live preview and confirm it arrives.
4. Domain management -> Add domain -> `idrpros.com` (primary), and add
   `www.idrpros.com` too.
5. DNS at GoDaddy (domain stays registered there; only records change):
   - `A` record, host `@` -> `75.2.60.5` (Netlify load balancer)
   - `CNAME` record, host `www` -> `<site-name>.netlify.app`
   - Remove any conflicting GoDaddy parking `A` record on `@` and any
     "forwarding" set on the domain.
   Confirm those values against what Netlify's domain panel shows before
   entering them; Netlify's panel is authoritative.
6. Email alias: the site publishes `dan@idrpros.com`. Set up forwarding
   to Dan's inbox (ImprovMX or GoDaddy email forwarding: MX + SPF TXT
   records at GoDaddy) and send a test message before launch.
7. Netlify issues the Let's Encrypt SSL certificate automatically once DNS
   resolves (Domain management -> HTTPS -> Verify DNS configuration).

## Spanish page (`/es/`)

- `es/index.html` is **generated** from `index.html` by `tools/make_es.py`
  (exact phrase replacement, English -> Spanish). Do not hand-edit it.
  After any change to `index.html`, run `python3 tools/make_es.py`. If an
  English phrase changed, the script stops and names it; update that pair
  in the script, then rerun.
- The Spanish form is a separate Netlify form, `claims-review-es`. Give it
  its own email notification (Forms -> Form notifications, or one set to
  "Any form"). Dropdown answers submit in English, so leads read the same.
- `es/gracias/` is the Spanish thank-you page (no-JS fallback).
- The logo image keeps its English taglines; its alt text is in Spanish.

## Before launch

1. **Netlify form notification** points at Dan's inbox, and a test
   submission from the live site arrives (Deploy step 3).
2. **`dan@idrpros.com` forwarding** is live and tested (Deploy step 6).
3. **National IDR figures** (88%, 2.7–4.5×, 300,000/month, 17×, 17–20%
   ineligible) are attributed in the footer to "publicly reported federal
   IDR data." If Dan has the specific CMS report, add the citation.

All results and claims about Dan's own practice are Dan's, as stated in
his newsletter. The compliance footer (attorney advertising, past results,
no attorney-client relationship) must remain on every page.

## Design system

- Colors: cream `#F7F2E8`, white, navy `#14243A` (text and dark
  sections), logo red `#BE0A12` (CTAs, key figures, accents), matched to
  the IDR Pros logo.
  Chosen to feel familiar to hospital and physician-group readers.
- Type: Newsreader (serif, headings and figures), IBM Plex Sans (body and
  small emphasis; no italics), IBM Plex Mono (small uppercase labels).
- The big logo leads the page; the header lockup appears only after it
  scrolls out of view.
- Compliance footer (attorney advertising, past results, no attorney-client
  relationship) must remain on every page ever added.
