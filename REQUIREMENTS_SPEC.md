# 📜 Requirements Specification – Stock Sage

> MoSCoW prioritization: **M**ust, **S**hould, **C**ould, **W**on’t (for now)

---

## 1 ▪ Functional Requirements

| ID | Requirement | Priority | Acceptance Criteria |
|----|-------------|----------|---------------------|
| **FR-01** | User can register & log in via email/password. | M | Given valid form → account created; invalid → error. |
| **FR-02** | Backend returns Top-10 stock lists (momentum, growth, value, watch) for current day. | M | `GET /suggestions` responds < 400 ms p95; 10 items per category. |
| **FR-03** | Each stock detail call includes TL;DR (≤120 words) + full rationale (≤700 words) + 3-day price range. | M | JSON has `summary`, `rationale`, `projection.low/high/confidence`. |
| **FR-04** | User can add suggestion to sandbox portfolio with virtual quantity & price. | M | Trade row persisted; portfolio endpoint reflects position. |
| **FR-05** | System recalculates unrealized/realized P/L every 30 min during market hours. | S | `/portfolio` shows up-to-date P/L. |
| **FR-06** | User can edit or delete sandbox positions. | C | CRUD ops logged; audit trail kept. |
| **FR-07** | Daily email summary of P/L (opt-in). | C | If opted, email sent at 18:00 ET. |

---

## 2 ▪ Non-Functional Requirements

| ID | Requirement | Priority | Acceptance Criteria |
|----|-------------|----------|---------------------|
| **NFR-01** | API median response ≤ 400 ms (95th ≤ 800 ms). | M | Locust load test @ 50 RPS passes. |
| **NFR-02** | Availability ≥ 99.5 % monthly. | M | Monitored via Statuspage. |
| **NFR-03** | All secrets managed in AWS SM / Fly Secrets; none in repo. | M | GitHub secret-scan passes CI gate. |
| **NFR-04** | Front-end Lighthouse performance ≥ 90. | S | Automated check in CI. |
| **NFR-05** | OWASP ZAP automated scan: zero High/Medium alerts. | S | CI gate must pass. |
| **NFR-06** | GDPR & CCPA-compliant data handling. | S | Data export & delete endpoints available. |

---

## 3 ▪ Assumptions & Constraints
* Market data via **yfinance** – subject to rate limits.  
* **Gemini Pro** rate-limit ≈ 60 requests/min (paid plan).  
* Paper trades value positions at end-of-minute close (not tick data).  

---

## 4 ▪ Acceptance-Test Format Example (Gherkin)

```gherkin
Feature: Add stock to sandbox

  Scenario: Successful virtual buy
    Given a logged-in user
    And the suggestions list includes "AAPL"
    When the user posts 5 shares of "AAPL" to /paper_trade
    Then the portfolio response contains a position for "AAPL"
    And the quantity equals 5
