# 🏗️ System Design – Stock Sage

> **Objective**   
> Deliver a secure, low-latency web platform that serves AI-generated stock insights and a real-time paper-trading sandbox to thousands of concurrent users.

---

## 1 ▪ Logical View

| Layer | Key Responsibilities | Tech |
|-------|----------------------|------|
| **Client (React SPA)** | Auth flows, dashboard UI, charts, PWA push notifications | React 18, Vite, TS, Recharts, Tailwind |
| **API Gateway / Web Tier** | HTTPS termination, CORS, rate-limiting, JWT cookie handling | Nginx (prod) / Fly edge (preview) |
| **Application Layer** | Business logic, Gemini orchestration, portfolio & risk services | Flask 3, SQLAlchemy, Celery |
| **Services** | • Market-data fetcher<br>• Paper-trade engine<br>• Notification worker | yfinance, ccxt, Redis broker |
| **Data Layer** | Persistent store + analytics | PostgreSQL 15, TimescaleDB ext |
| **AI Layer** | Prompt templates, rationale & prediction generation | Gemini Pro via google-generativeai |
| **Observability** | Metrics, logs, tracing, alerting | Prometheus, Grafana, Loki, PagerDuty |
| **CI/CD & Infra** | Build, test, deploy, IaC, secrets | GitHub Actions, Docker, AWS Fargate, Terraform |

---

## 2 ▪ Component Diagram (Mermaid)

```mermaid
graph TD
  subgraph Frontend
    R[React SPA<br/>(Vite + TS)]
  end

  subgraph Edge
    G[NGINX / Fly Proxy]
  end

  subgraph Backend
    F[Flask API]
    SVC[Paper-Trade<br/>Service]
    MD[Market Data<br/>Fetcher]
    CEL[Celery Workers]
  end

  subgraph Data
    PG[(PostgreSQL 15<br/>+ Timescale)]
    REDIS[(Redis Broker)]
  end

  subgraph AI
    GEM[Gemini Pro]
  end

  %% flows
  R -->|HTTPS REST| G --> F
  F -->|LLM Call| GEM
  F -->|ORM| PG
  F -->|publish task| REDIS --> CEL
  CEL -->|update P/L| PG
  CEL --> SVC
  SVC --> MD -->|quotes| PG

  %% monitoring
  F -- logs --> LG[Grafana Loki]
  F -- metrics --> PM[Prometheus]

  classDef store fill:#f9f,stroke:#333,stroke-width:1px;
