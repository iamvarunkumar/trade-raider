# 🏃‍♂️ Sprint Plan – Q2 2025 (2-week cadences)

| Sprint | Dates (Asia/Kolkata) | Goals / Stories | Acceptance |
|--------|----------------------|-----------------|------------|
| **Sprint 0** | Apr 28 – May 11 | • CI/CD scaffold<br>• Dev env Docker files<br>• Auth skeleton<br>• DB migrations baseline | PR merges green; `fly launch` preview up |
| **Sprint 1** | May 12 – May 25 | • Email/password auth + JWT<br>• `/suggestions` endpoint (static mock)<br>• React login & dashboard shell | User logs in; sees mock Top-10 cards |
| **Sprint 2** | May 26 – Jun 8 | • Gemini integration<br>• Real Top-10 generation logic<br>• Stock Detail page with TL;DR/full rationale | Live AI picks; 95 % tests pass |
| **Sprint 3** | Jun 9 – Jun 22 | • Sandbox paper-trade CRUD<br>• P/L calc service<br>• Portfolio page w/ Recharts line graph | Add/edit/delete trades; P/L updates |
| **Sprint 4** | Jun 23 – Jul 6 | • Harden security (rate-limit, CSP)<br>• Lighthouse ≥ 90<br>• README & docs polish<br>• Beta launch on staging | OWASP scan clean; staging link to testers |

**Definition of Done**  
1. Code merged to `main`.  
2. Tests + lint green.  
3. Docs updated.  
4. Deployed to staging. 
