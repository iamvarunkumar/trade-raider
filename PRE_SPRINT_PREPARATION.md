# 🏁 Pre-Sprint Preparation – Trade Baiter

> **Purpose**  
> Ensure the team, backlog, and environments are fully readied before Sprint 0 kicks off on **1 May 2025**.

---

## 1 ▪ Objectives

| # | Outcome |
|---|---------|
| 1 | Shared understanding of vision, scope, and MVP (see `PROJECT_OVERVIEW.md`). |
| 2 | Groomed Product Backlog with MoSCoW priorities & story points. |
| 3 | Development environments reproducible via Dev-container / Docker. |
| 4 | CI pipeline green (lint, tests, Docker build). |
| 5 | Core governance docs ratified (SOP Security, DevOps, Test Strategy). |
| 6 | Risks & dependencies logged with mitigation owners. |

---

## 2 ▪ Timeline (Asia/Kolkata)

| Date | Activity | Owner(s) |
|------|----------|----------|
| **22 Apr 2025** | Kick-off workshop (vision, personas) | PM, Product |
| 23–24 Apr | Backlog refinement & story pointing | Dev team, QA |
| 25 Apr | Architecture deep-dive & threat model | Lead Arch, Sec |
| 26 Apr | Dev-container & Dockerfile freeze | DevOps |
| 27 Apr | CI pipeline smoke run + Docs review | DevOps, QA |
| **28 Apr** | Sprint 0 planning & commitment | All |

---

## 3 ▪ Deliverables

1. **Backlog v1** in Jira/Linear with EPICs, user stories, acceptance criteria, story points.  
2. **Branching model** implemented (`main`, `dev`, `feature/*`, `hotfix/*`).  
3. **CI Workflow** (`lint`, `pytest`, `docker-build`) passing on `dev`.  
4. **Dev Environment Guide** (`DEV_SETUP.md`) verified on Windows+macOS+Linux.  
5. **Risk Register** with likelihood × impact matrix.  
6. **Communication Charter** (Slack channels, daily stand-up time, demo cadence).  

---

## 4 ▪ Key Tasks & Checklist

| ☑ | Task | Ref |
|----|------|-----|
| ☐ | Create GitHub repo, enable branch protection on `main` | SOP_DEVOPS §1 |
| ☐ | Import core docs (`README`, SOPs, System Design) | earlier files |
| ☐ | Add Dependabot, CodeQL, secret-scan actions | SOP_SECURITY §6 |
| ☐ | Finalize Docker base images (python:3.12-slim, node:18-alpine) | SOP_DEVOPS §3 |
| ☐ | Write minimal Flask “hello” w/ healthcheck & unit test | Sprint 0 backlog |
| ☐ | Configure Fly.io preview app (`fly launch`) | Sprint 0 backlog |
| ☐ | Establish Story-point baseline (Fibonacci 1-3-5-8-13) | Team |
| ☐ | Document Definition of Ready & Done | TEST_STRATEGY.md |
| ☐ | Schedule recurring ceremonies (stand-up, backlog groom, retro) | Scrum Master |
| ☐ | Sign-off on security controls (JWT expiry, rate-limits) | Sec Specialist |

---

## 5 ▪ Roles & Responsibilities

| Role | Name | Key Pre-Sprint Duties |
|------|------|-----------------------|
| Product Manager | (TBD) | Own backlog, acceptance criteria |
| Scrum Master | (TBD) | Facilitate ceremonies, remove blockers |
| Tech Lead | (TBD) | Finalize architecture, review PRs |
| DevOps | (TBD) | CI/CD, infra-as-code |
| QA Lead | (TBD) | Test plan, coverage thresholds |
| Security Champ | (TBD) | Threat model, dependency scans |

> *Fill “TBD” names during kick-off.*

---

## 6 ▪ Risk & Mitigation Snapshot

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Gemini rate-limit throttles `/suggestions` | Medium | High | Caching layer, exponential back-off |
| yfinance API schema change | Low | Medium | Version pin, fallback to Alpha Vantage |
| Team bandwidth (holidays) | Medium | Medium | Adjust Sprint velocity, cross-training |
| Regulatory disclaimer gaps | Low | High | Legal review before public beta |

---

## 7 ▪ Tools Matrix

| Need | Tool | Note |
|------|------|------|
| Source control | GitHub Enterprise | repo: *stocksage* |
| Issue tracking | Jira / Linear | tag “Q2-MVP” |
| CI/CD | GitHub Actions | yaml in `.github/workflows/` |
| Container registry | GHCR (preview) → ECR (prod) | automated tags |
| Docs | Markdown + Mermaid | diagrams rendered in PR |
| Comms | Slack | channels: `#sage-dev`, `#sage-qa` |

---

*Prepared 1 May 2025 – Trade Baiter PMO.* 
