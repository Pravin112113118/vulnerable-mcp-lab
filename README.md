# ⚠️ Vulnerable MCP Lab (Educational Only)

This project demonstrates common web vulnerabilities using FastAPI.

## 🚨 WARNING
Do NOT deploy this in production. This is for learning purposes only.

## 🔥 Vulnerable Endpoints

### SQL Injection
`/vuln/user?username=' OR 1=1--`

### SSRF
`/vuln/fetch?url=http://example.com`

### Insecure Deserialization
POST to `/vuln/deserialize`

### Debug Leak
`/vuln/debug`

### Auth Bypass
`/vuln/admin?token=admin`

---

## ✅ Safe Endpoints
- `/safe/health`
- `/safe/hello`

---

## 🚀 Run locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
