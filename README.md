# 🐍📈 Trade Baiter – Flask + React Paper-Trading & AI Insight Platform

Stock Sage is a full-stack web application that helps retail investors **discover, understand, and safely paper-trade** promising equities.  
It combines:

* **Flask 3.x REST API** – authentication, analytics & Gemini AI orchestration  
* **React 18 SPA** – rich dashboards, TL;DR cards, and a sandbox portfolio  
* **Gemini Pro** – rationale generation & 3-day price outlooks  
* **PostgreSQL** – user accounts, predictions, simulated trades  

> **⚠️ Disclaimer** – Stock Sage offers *informational* insights only and does **not** constitute financial advice. Predictions are probabilistic and limited to a 3-day horizon to reduce over-promising risk.

---

## 1 ▪ Architecture

┌───────────────┐ fetch/submit ┌───────────────────────┐ │ React SPA │ ↔ REST (JSON/CORS) ↔ │ Flask API + Gemini AI │ │ (Vite + TS) │ │ • auth • inference │ └───────────────┘ └──────────┬────────────┘ │ SQLAlchemy ┌───────────────▼───────────────┐ │ PostgreSQL 15 DB │ │ users • symbols • predictions │ │ paper_trades • watchlists │ └───────────────────────────────┘

yaml
Copy
Edit

---

## 2 ▪ Key Features

| Screen | Highlights |
|--------|------------|
| **Dashboard** | Top-10 Movers • Growth-Plays • Value Picks • TL;DR cards |
| **Stock Detail** | Full Gemini narrative • fundamentals • technical chart |
| **Sandbox Portfolio** | Add suggestions → virtual trades → P/L chart & log |

---

## 3 ▪ Quick Start (Dev)

```bash
# Back-end
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # add GEMINI_API_KEY, JWT_SECRET, DATABASE_URL
flask --app api run

# Front-end
cd frontend
pnpm install
pnpm dev
