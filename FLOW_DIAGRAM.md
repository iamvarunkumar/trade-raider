# 🔄 End-to-End Flow Diagram – Stock Sage

```mermaid
sequenceDiagram
    autonumber
    actor User as 👤 User (Browser)
    participant FE as 🖥️ React SPA
    participant API as 🐍 Flask API
    participant MD as 📈 Market-Data Fetcher
    participant GEM as 🤖 Gemini Pro
    participant DB as 🗄️ PostgreSQL
    participant CEL as ⚙️ Celery Worker

    %% 1 ▪ Auth
    User->>FE: Enter email & password
    FE->>API: POST /auth/login
    API->>DB: Verify credentials
    DB-->>API: OK / Fail
    API-->>FE: JWT (HttpOnly cookie)

    %% 2 ▪ Dashboard Suggestions
    User->>FE: Navigate to Dashboard
    FE->>API: GET /suggestions (JWT)
    alt Cached
        API-->>FE: JSON lists (Top-10)
    else Cold path
        API->>MD: Fetch latest quotes
        API->>GEM: Prompt – features → narrative + 3-day range
        GEM-->>API: Rationale & projection
        API->>DB: Persist predictions
        API-->>FE: JSON lists
    end

    %% 3 ▪ Stock Detail
    User->>FE: Click stock card
    FE->>API: GET /stock/{symbol}
    API-->>FE: TL;DR • full rationale • metrics

    %% 4 ▪ Add to Sandbox
    User->>FE: “Add to Sandbox” (+qty, price)
    FE->>API: POST /paper_trade
    API->>DB: Insert trade row
    API-->>FE: Confirmation

    %% 5 ▪ Scheduled P/L Updates
    Note over CEL,DB: Every 30 min (market hours)
    CEL->>DB: Query open positions
    CEL->>MD: Pull fresh quotes
    CEL->>DB: Update P/L & snapshots

    %% 6 ▪ (Phase 2) Live Push
    CEL--)-FE: WebSocket/SSE P/L delta
    FE-->>User: Updated portfolio chart
