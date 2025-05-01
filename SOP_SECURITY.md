# 🔐 Security SOP – Trade Raider

## 1 ▪ Principles
1. **Least Privilege** – Minimal IAM roles for services.  
2. **Shift-left** – Static analysis (Bandit) and SCA (Dependabot) in PR.  
3. **Zero Secrets in Git** – Use `fly secrets` (preview) / AWS SM (prod).  
4. **Defense-in-Depth** – Multiple layers: WAF, JWT auth, RBAC, DB row-level perms.  

---

## 2 ▪ Authentication & Session
* Bcrypt-hashed passwords (`passlib[bcrypt]`, 12 rounds).  
* JWT access token (15 min) + refresh (7 days) stored in **HttpOnly** cookies.  
* Rotate JWT signing key monthly; invalidate on password change.  

---

## 3 ▪ API Hardening
| Control | Tool/Setting |
|---------|--------------|
| Rate limiting | Flask-Limiter: 100 req/min per IP |
| CORS | Explicit origins list (`localhost:5173`, prod domain) |
| Input validation | Pydantic v2 models |
| Security headers | `flask-talisman` – CSP, HSTS(1yr), X-Frame-Options DENY |

---

## 4 ▪ Data Protection
* PostgreSQL-AES-256 at rest (AWS RDS).  
* TLS 1.3 mandatory; certs via Let’s Encrypt.  
* Daily encrypted snapshots (30-day retention).  

---

## 5 ▪ Gemini Usage
* No PII in prompt context.  
* System message includes: “Provide financial education, not advice.”  
* Log only hashed user ID & token usage metrics.  

---

## 6 ▪ Vulnerability Management
1. Dependabot alerts triaged daily.  
2. Critical CVE patch within 24 h; High within 72 h.  
3. Quarterly external penetration test. 
