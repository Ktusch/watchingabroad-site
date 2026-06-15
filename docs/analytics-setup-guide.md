# Analytics Setup Guide for WatchingAbroad

**Mål:** Google Search Console + GA4 + rank tracking operational
**Deadline:** Først i uge 26 (helst 14-16 juni)

---

## 1. Google Search Console — 🔴 Gør dette nu

### Trin 1: Tilføj domæne i GSC
1. Gå til https://search.google.com/search-console/welcome
2. Log ind med **kt@medtech-advisors.com** (brug passkey)
3. Vælg **"Domain"** (ikke "URL prefix")
4. Indtast: `watchingabroad.com`
5. Vælg **DNS TXT record verification**

### Trin 2: Tilføj DNS TXT record via Simply.com
Da jeg ikke har Simply.com API-adgang, skal du selv tilføje TXT-recorden:
1. Log ind på Simply.com → DNS-indstillinger for watchingabroad.com
2. Tilføj den TXT-record som Google giver dig (noget ala `google-site-verification=...`)
3. Vent 5-10 minutter og klik "Verify" i GSC

### Trin 3: Submit sitemap
Når domænet er verificeret:
1. I GSC → Sitemaps → "Add a new sitemap"
2. Indtast: `sitemap.xml`
3. Klik Submit

**Sitemap er allerede live:** https://watchingabroad.com/sitemap.xml
**Robots.txt er allerede live:** https://watchingabroad.com/robots.txt

---

## 2. Google Analytics 4 (GA4)

### Opret GA4 property
1. Gå til https://analytics.google.com/
2. Log ind med kt@medtech-advisors.com
3. Opret nyt property: "WatchingAbroad"
4. Indstil tidszone: Europe/Copenhagen, valuta: EUR
5. Vælg "Web" som data stream
6. Web URL: https://watchingabroad.com
7. Stream name: "WatchingAbroad Web"
8. **Kopier Measurement ID** (format: `G-XXXXXXXXXX`)

### Aktiver tracking på sitet
GA4 tracking stub er **allerede tilføjet** til alle 3 sider med placeholder `G-XXXXXXXXXX`:
- `index.html`
- `guides/why-we-built-watchingabroad.html`
- `guides/smart-dns-vs-vpn.html`

**Du skal:** Erstat `G-XXXXXXXXXX` med det rigtige Measurement ID i alle 3 filer.
Gør det på GitHub: https://github.com/Ktusch/watchingabroad-site/tree/main

---

## 3. Rank Tracker

En CSV-skabelon er gemt i projektet:
`~/workspace/40_Projects/watchingabroad/docs/rank-tracker-template.csv`

### Opret Google Sheet
1. Gå til https://sheets.new
2. File → Import → Upload → vælg CSV'en
3. Del arket med kt@medtech-advisors.com
4. Udfyld positionskolonnen ugentligt (tjek GSC → Search results → Average position)

### Alternativ: Gør via mig (Sophia)
Når Sheets API er aktiveret i Google Cloud Console (se nedenfor), kan jeg oprette arket automatisk.

---

## 4. Enable manglende Google APIs

Google Cloud projektet skal have aktiveret nogle APIs. Tokenet har scopes til Sheets/Drive/Gmail/Calendar, men **ikke** til at enable APIs eller til Search Console/GA4.

### Aktivering (gør én gang):
1. Gå til https://console.cloud.google.com/apis/library?project=804064994495
2. Log ind med kt@medtech-advisors.com
3. Søg og **Enable** disse APIs:
   - **Google Sheets API** (så rank tracker kan oprettes programmatisk)
   - **Search Console API** (så data kan hentes)
   - **Google Analytics Admin API** (så GA4 kan administreres)
4. Hvis nødvendigt: gå til OAuth consent screen og tilføj bruger

### Opdater OAuth scopes (hvis ovenstående ikke er nok):
1. Gå til https://console.cloud.google.com/apis/credentials?project=804064994495
2. Rediger OAuth 2.0 Client ID (desktop app)
3. Tilføj scopes: `https://www.googleapis.com/auth/webmasters`, `https://www.googleapis.com/auth/analytics`
4. Kør setup.py igen for at re-authenticate:
```bash
GSETUP="python3 ~/.hermes/profiles/sophia/skills/productivity/google-workspace/scripts/setup.py"
$GSETUP --auth-url --services calendar,drive,sheets,docs,gmail,webmasters,analytics
```
5. Åbn URL'en, log ind, kopier redirect URL'en tilbage

---

## Status (14. juni 2026)

| Item | Status | Notes |
|------|--------|-------|
| Sitemap.xml | ✅ Live | GitHub Pages |
| Robots.txt | ✅ Live | Refererer til sitemap |
| GA4 tracking stub | ✅ Placed | Skal have rigtig G-ID |
| GSC ownership | ❌ Mangler | DNS TXT record + verification |
| Rank tracker | ⏳ Template klar | CSV template i /docs |
| Sheets API | ❌ Skal enables | Google Cloud Console |
| GSC/GA4 APIs | ❌ Skal enables | Google Cloud Console |

**Anbefalet rækkefølge:** Enable APIs (5 min) → GSC DNS TXT (10 min) → GA4 property (10 min) → Replace G-ID (2 min)
