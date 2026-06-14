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
└── guides/
    ├── why-we-built-watchingabroad.html   ✅ LIVE (13. juni)
    └── smart-dns-vs-vpn.html              ✅ LIVE (13. juni)
```

---

## Affiliate-programmer (tilmeldt)

| Nuværende | Status |
|---|---|
| Smart DNS Proxy | ❌ Ikke ansøgt endnu |
| NordVPN | ❌ Ikke ansøgt endnu |
| Surfshark | ❌ Ikke ansøgt endnu |

Indtil affiliate-ansøgninger er godkendt: **ingen kommercielle links der lover kommission.**  
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
