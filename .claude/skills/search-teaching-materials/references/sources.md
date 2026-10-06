# Source catalogue

`scripts/search_sources.py --list` shows which connectors have keys. Keys go in
`.claude/skills/search-teaching-materials/.env` (git-ignored) or
`~/.config/teaching-search/.env`; copy `.env.example`.

## Open APIs (no key or free key)

| Connector | Covers | Key | Notes |
|---|---|---|---|
| openalex | 250M+ works: articles, books, chapters, reports, datasets; author pages | none (`OPENALEX_EMAIL` for polite pool) | best first stop; `filter=type:` per category |
| crossref | DOI metadata: articles, books, reports | none (`CROSSREF_EMAIL`) | authoritative bibliographic data, abstracts partly |
| semantic_scholar | articles with citation counts, open PDFs | optional `S2_API_KEY` (free) | 100 req/5 min without key |
| core | open-access full texts, working papers, theses | `CORE_API_KEY` (free, core.ac.uk) | full-text PDFs for Dropbox |
| doaj | open-access journal articles | none | |
| arxiv | preprints (stat.ML, econ.EM, cs) | none | Atom XML |
| openlibrary | book metadata, editions, ISBN | none | |
| google_books | book metadata, descriptions | optional `GOOGLE_API_KEY` | 1,000 req/day with key |
| youtube | videos, playlists | `YOUTUBE_API_KEY` | Google Cloud Console → enable "YouTube Data API v3" → Credentials → API key; free 10,000 units/day (a search costs 100) |
| github | repositories: packages, notebooks, course material | optional `GITHUB_TOKEN` | 10 req/min unauthenticated |
| zenodo | datasets, software, slides, teaching material | none | |
| harvard_dataverse | research datasets | none | |
| kaggle | datasets | `KAGGLE_USERNAME` + `KAGGLE_KEY` (kaggle.com → Settings → API) | |
| data_europa | EU open data portal | none | |
| data_gov | US open data | none | |

Also usable through MCP / web search in Claude Code: Consensus (`mcp__Consensus__search`,
semantic paper search), web search for publisher pages, course platforms, blogs, people.
Data portals without a connector: Eurostat (SDMX API), OECD (SDMX), World Bank API,
Statistik Austria (open data portal), Our World in Data; search them via web search and
link the dataset page.

## WU-licensed databases

WU Bibliothek uses Ex Libris Alma with two Primo front ends ("WU-Katalog" and
"CatalogPLUS"). Database list: https://www.wu.ac.at/bibliothek/recherche/datenbanken/.
Confirmed licences (database info pages under `.../datenbanken/info/<name>`): Scopus, Web of
Science Core Collection, EBSCO Business Source Premier, ABI/Inform (ProQuest), JSTOR, Emerald,
wiso, Statista, Passport (Euromonitor), Orbis / Orbis Europe, LSEG Workspace, WRDS, Factiva,
Panjiva. SpringerLink e-book collections are likely but were not confirmed on a WU page.

| Connector | Database | Key / credential | How to obtain |
|---|---|---|---|
| wu_primo | WU catalogue + CatalogPLUS (books, e-books, articles, cases held by WU) | `PRIMO_API_KEY`, `PRIMO_VID`, optional `PRIMO_API_HOST`, `PRIMO_SCOPE`, `PRIMO_TAB`, `PRIMO_DISCOVERY_BASE` | Ask WU Bibliothek (systems librarian) for a Primo Search API key from the Ex Libris Developer Network and for the view ID (vid) and scope of CatalogPLUS. This is the single most valuable key: it answers "does WU have it?" directly. |
| scopus | Scopus abstracts and citations | `ELSEVIER_API_KEY`, optional `ELSEVIER_INSTTOKEN` | Register at dev.elsevier.com with WU e-mail; the key works from the WU network/VPN; for off-campus use request an institutional token via the library. |
| wos | Web of Science Starter API | `CLARIVATE_WOS_API_KEY` | developer.clarivate.com → register → "Web of Science Starter API" (free tier for subscribing institutions). |
| springer | Springer Nature Meta API (books, chapters, journals) | `SPRINGER_API_KEY` | dev.springernature.com, free; metadata is open, full text through the WU licence. |
| ebsco_eds | EBSCO Discovery Service (Business Source Premier etc.) | `EDS_USER`, `EDS_PASSWORD`, `EDS_PROFILE` | Only if WU has an EDS profile (uncertain; WU uses Primo). Ask the library. Connector untested. |

No usable search API under an academic licence: Statista, Passport, Orbis, LSEG, Factiva,
JSTOR (Constellate retired), Emerald, ProQuest (TDM Studio separate), Harvard Business
Publishing, The Case Centre, Ivey, SAGE Business Cases. Search these via web search and the
vendor sites; link the record and add "WU-Lizenz prüfen" or "per Kurs zu lizenzieren" (for
cases).

## Case collections

- Harvard Business Publishing Education: https://hbsp.harvard.edu/ (educator account; cases
  bought per course)
- The Case Centre: https://www.thecasecentre.org/ (educator registration; free cases exist)
- Ivey Publishing: https://www.iveypublishing.ca/
- SAGE Business Cases: https://sk.sagepub.com/cases
- Emerald Emerging Markets Case Studies: https://www.emerald.com/insight/publication/issn/2045-0621
- WU EMCEE case collection: https://www.wu.ac.at/emcee/lehre/lehrmaterialien/fallstudien-emerging-markets-cee/
- Open teaching labs with data: ISLP/ISLR labs, UC Berkeley Data 100, MIT OCW, Stanford
  Online, Kaggle Learn, Posit Cloud primers

## Network note

In Claude Code cloud sessions most API hosts are blocked by the environment's network
policy (only package registries pass). Run the skill on a PC, or add the hosts to the
environment's allowed domains: api.openalex.org, api.crossref.org,
api.semanticscholar.org, api.core.ac.uk, doaj.org, export.arxiv.org, openlibrary.org,
www.googleapis.com, api.springernature.com, api.elsevier.com, api.clarivate.com,
api-eu.hosted.exlibrisgroup.com, api.github.com, zenodo.org, dataverse.harvard.edu,
www.kaggle.com, data.europa.eu, catalog.data.gov, content.dropboxapi.com, api.dropboxapi.com.
