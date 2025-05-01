# Trade-Raider
# 🐍📈 Stock Sage – Flask + React Paper-Trading & AI Insight Platform

Stock Sage is a full-stack web application that helps retail investors **discover, understand, and safely paper-trade** promising equities.  
It combines:

* **Flask 3.x REST API** – authentication, analytics & Gemini AI orchestration  
* **React 18 SPA** – rich dashboards, TL;DR cards, and a sandbox portfolio  
* **Gemini Pro** – rationale generation & 3-day price outlooks  
* **PostgreSQL** – user accounts, predictions, simulated trades  

> **⚠️ Disclaimer** – Stock Sage offers *informational* insights only and does **not** constitute financial advice. Predictions are probabilistic and limited to a 3-day horizon to reduce over-fitting risk.

---

## 1. Architecture ➜

┌───────────────┐ fetch/submit ┌───────────────────────┐ │ React SPA │ ↔ REST (JSON/CORS) ↔ │ Flask API + Gemini AI │ │ (Vite + TS) │ │ • auth • inference │ └───────────────┘ └──────────┬────────────┘ │ SQLAlchemy ┌───────────────▼───────────────┐ │ PostgreSQL 15 DB │ │ users • symbols • predictions │ │ paper_trades • watchlists │ └───────────────────────────────┘

yaml
Copy
Edit

* **Flow** – Front-end requests `/suggestions` → Flask fetches market data (`yfinance`), builds a feature vector, calls Gemini for narrative + 3-day outlook, persists result, responds to SPA.  
* **Sandbox** – Paper-trade engine computes unrealized / realized P/L with intraday polling.

---

## 2. Key Features

| Screen | Highlights |
|--------|------------|
| **Dashboard** | Top-10 Movers • Growth-Plays • Value Picks • TL;DR cards |
| **Stock Detail** | Full Gemini narrative • fundamentals • technical chart |
| **Sandbox Portfolio** | Add suggestions → virtual trades → P/L chart & log |

---

## 3. Quick Start (Dev)

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

# == Core ==
Flask~=3.0.2          # lightweight web framework
Flask-CORS~=4.0.0     # CORS headers
SQLAlchemy~=2.0.30    # ORM
psycopg[binary]~=3.1  # PostgreSQL driver

# == Auth & Security ==
flask-jwt-extended~=4.6
passlib[bcrypt]~=1.7

# == AI & ML ==
google-generativeai~=0.4.0   # Gemini Pro client
pandas~=2.2
scikit-learn~=1.4
prophet~=1.2                 # time-series baseline (requires pystan)

# == Market Data ==
yfinance~=0.2
ccxt~=4.2          # optional multi-exchange quotes

# == Utilities ==
python-dotenv~=1.0
pydantic~=2.7      # request/response schemas
gunicorn~=22.0     # prod WSGI server
alembic~=1.13      # migrations

# == Dev/Test ==
pytest~=8.2
pytest-cov~=5.0
black~=24.4
isort~=5.13
