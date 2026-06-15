# WatchingAbroad — Source of Truth

> **Formål:** Én autoritativ reference for alt der kan gå galt: konti, emails, domæner, affiliates, godkendelser.
> **Regel:** ALDRIG publicer content der refererer til noget der ikke står i dette dokument.

---

## Domæne

| Felt | Værdi |
|---|---|
| Domæne | watchingabroad.com |
| Registrator | Simply.com |
| DNS | Simply.com nameservers (ns1-4.simply.com) |
| Udløb | 1. august 2026 (sammenfaldende med kill switch) |
| Hosting | GitHub Pages (Ktusch/watchingabroad-site) |
| HTTPS | ✅ Let's Encrypt via GitHub Pages — VERIFICERET 14. juni 2026 |

---

## Email — KUN disse adresser findes

| Alias | Viderestiller til | Status |
|---|---|---|
| admin@watchingabroad.com | (direkte mailboks) | ✅ Oprettet, SMTP testet |
| atlas@watchingabroad.com | admin@watchingabroad.com | ✅ Oprettet |

**❌ Oprettes automatisk:** `hello@`, `ceo@`, `editor@`, `support@`, `info@`

> **Regel:** Brug KUN `admin@watchingabroad.com` i publiceret content hvis du skal have en kontaktadresse.  
> **Brug aldrig** en email der ikke står i tabellen ovenfor.

> **Opdateret 14. juni:** `mailto:admin@watchingabroad.com` er nu aktiv på `why-we-built-watchingabroad.html` — erstattet den tidligere `href="#"` placeholder.

---

## Site struktur

```
watchingabroad.com/
├── index.html                    (landing page)
├── CNAME                         (watchingabroad.com)
├── .nojekyll
├── sitemap.xml                   (10 URLs, opdateret 15. juni)
├── robots.txt                    (Allow: /, Sitemap: /sitemap.xml)
├── disclosure/
│   └── index.html                (EU affiliate disclosure page ✅ 15. juni)
├── go/
│   ├── index.html                (affiliate redirect landing page)
│   ├── config.json               (vendor config — update target_url når links er aktive)
│   ├── smart-dns-proxy/index.html
│   ├── nordvpn/index.html
│   ├── surfshark/index.html
│   ├── pia/index.html
│   ├── cyberghost/index.html
│   ├── vyprvpn/index.html
│   └── windscribe/index.html
├── scripts/
│   ├── pre-publish-check.py      (compliance checker)
│   └── generate-affiliate-redirects.py  (gen. redirect pages from config.json)
└── guides/
    ├── why-we-built-watchingabroad.html               ✅ LIVE (13. juni)
    ├── smart-dns-vs-vpn.html                          ✅ LIVE (13. juni)
    ├── how-to-setup-smart-dns-apple-tv-fire-tv-router.html  ✅ LIVE (14. juni)
    ├── best-smart-dns-streaming.html                  ✅ LIVE (14. juni)
    ├── watch-streaming-while-travelling-checklist.html ✅ LIVE (14. juni)
    ├── vpn-apple-tv-options-limitations-setup.html    ✅ LIVE (14. juni)
    ├── best-vpn-for-expats-2026.html                   ✅ LIVE (15. juni)
    └── how-to-watch-bbc-iplayer-abroad.html            ✅ LIVE (15. juni) — schema.org markup: Article + BreadcrumbList + FAQPage (8 questions)
```

---

## Affiliate-programmer

| Område | Status |
|---|---|
| Smart DNS Proxy | 🔴 Afventer Kristian-godkendelse (self-serve, skal bruge password) |
| NordVPN | ❌ Ikke ansøgt — kræver 5+ artikler + Kristian approval |
| Surfshark | ❌ Ikke ansøgt — kræver Kristian approval |
| /go/ redirect infrastructure | ✅ Bygget — 7 vendor redirect pages live, config-drevet |
| /disclosure/ page | ✅ Bygget — EU compliance klar, fuld disclosure side live |
| Accessible from footer | ✅ index.html footer opdateret med disclosure + go links |
| EU disclosure research | ✅ Done — se docs/eu-affiliate-disclosure-compliance.md |

**Indtil affiliate-ansøgninger er godkendt:** `go/config.json` har tomme `target_url` felter — redirect pages viser "Coming soon" placeholder.  
**Når Kristian leverer affiliate URLs:** opdater `go/config.json` og kør `scripts/generate-affiliate-redirects.py`.  
Brug `rel="nofollow sponsored"` på affiliate links når de er aktive.

---

## Godkendelsesmatrix

| Handling | Kræver godkendelse |
|---|---|
| Publicere ikke-kommerciel artikel | Compliance-tjek + source-of-truth validering |
| Publicere kommerciel artikel / affiliate links | Kristian approval |
| Ændre email / DNS / domæne | Kristian approval |
| Slette content | Kristian approval |
| Skrive om juridiske eller medicinske emner | Kristian approval |

---

## Content compliance checklist (pre-publish)

Hvert stykke content SKAL bestå disse tjek før publicering:

- [ ] 1. **Source of Truth audit** — alle referencer (emails, URLs, navne) findes i Source of Truth
- [ ] 2. **Affiliate disclosure** — `rel="nofollow sponsored"` på kommercielle links
- [ ] 3. **Ingen placeholder-content** — ingen "lorem ipsum", "coming soon", "TODO"
- [ ] 4. **Ingen ødelagte links** — alle interne links (`/guides/...`) peger på eksisterende filer
- [ ] 5. **Datoer** — published/updated dater er korrekte
- [ ] 6. **Ingen overclaims** — ingen garantier om at "X virker altid med Y"
- [ ] 7. **Sprog** — klart engelsk, ingen markedsførings-hype
