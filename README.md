# idrpros.com

IDR Pros ("Maximizing what you're owed"), serviced by Smith Law:
Dan Smith, Esq., Tampa. Audience: Florida out-of-network providers, physician
groups, and hospital systems. Content is adapted from Dan's newsletter,
"IDR Is Just the Beginning: How Florida Law Recovers What IDR Cannot."

Static single-page site. No build step. No dependencies. No server.

## Files

- `index.html`: the entire site (markup, CSS, JS inline)
- `thanks/index.html`: form confirmation page (used when JS is off)
- `fonts/`: self-hosted Newsreader, IBM Plex Sans, IBM Plex Mono (woff2)
- `img/idrpros-logo.png`: full logo with both taglines, transparent (from Dan's logo file)
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

## PRE-LAUNCH GATES: do not point idrpros.com at this until cleared

Florida Bar advertising rules (Chapter 4-7) apply to lawyer websites, and
Morgan & Morgan will likely want its marketing and compliance team to
review anything carrying the firm name.

1. **Smith Law and the trade name.** The site presents IDR Pros as "a trade
   name of Smith Law." Florida permits trade names only if they are not
   misleading and the lawyer actually practices under them; confirm Smith
   Law is formed and in good standing, and that Dan practices as IDR Pros.
   "Pros" can be read as a claim of expertise (Rule 4-7.14 restricts
   "expert"/"specialist" absent certification); have Dan confirm he is
   comfortable with the name.
2. **Morgan & Morgan.** The flyer was written as Morgan & Morgan; this
   site names Smith Law only. The M&M results in the flyer (below) may
   belong to that firm. Confirm Dan may cite them as his own, and how
   (Florida requires past results be the advertising lawyer's own).
2a. **Office location and phone.** Rule 4-7.12 requires the city of a bona
   fide office. The site says "Tampa, Florida" and uses (813) 523-3134,
   both taken from the M&M-era flyer. Confirm both are Smith Law's.
3. **Past results must be objectively verifiable (Rule 4-7.13).** Confirm
   Dan can document each of these: 90%+ IDR win rate; $1M+ for a single
   hospital group; in-network rates 3× prior levels; "hundreds of lawsuits
   across thousands of claims ... all resolved by settlement or plaintiff
   judgment"; "hundreds" of ERISA preemption orders since 2017.
4. **"0 losses" on ERISA preemption.** The flyer headline says "Zero
   Losses," and the site shows it as a stat tile. This is the claim most
   likely to draw a compliance question. Keep, soften, or cut.
5. **National IDR figures.** 88% provider win rate, 2.7–4.5× QPA,
   300,000 disputes a month, 17× projections, 17–20% ineligible. The
   footer attributes these to "publicly reported federal IDR data." Get the
   specific CMS report and date from Dan, and ideally cite it on the page.
6. **Four-year lookback.** Confirm the limitations period Dan relies on.
7. **Comparison table** (Federal IDR vs. Florida law, "Florida law"
   section). This is new; it is not in the flyer. Dan should confirm each
   row, especially "Discovery: None" and "Review: Very limited" for IDR.
8. **Intake email.** Leads go wherever the Netlify form notification is
   pointed (step 3 above). The published address `dan@idrpros.com` must
   forward somewhere before launch (step 6). The form tells users not to send PHI.

## Design system

- Colors: cream `#F7F2E8`, white, navy `#14243A` (text and dark
  sections), logo red `#BE0A12` (CTAs, key figures, accents), matched to
  the IDR Pros logo.
  Chosen to feel familiar to hospital and physician-group readers.
- Type: Newsreader (serif, headings and figures), IBM Plex Sans (body),
  IBM Plex Mono (small uppercase labels).
- Compliance footer (attorney advertising, past results, no attorney-client
  relationship) must remain on every page ever added.
