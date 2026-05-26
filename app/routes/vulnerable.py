from fastapi import APIRouter, Query
import requests
import pickle
import base64

router = APIRouter()

# 1. ❌ SQL Injection Simulation
@router.get("/user")
def get_user(username: str):
    query = f"SELECT * FROM users WHERE username = '{username}'"
    return {"query_executed": query}


# 2. ❌ SSRF (simulated)
@router.get("/fetch")
def fetch_url(url: str):
    try:
        r = requests.get(url)
        return {"status": r.status_code, "content": r.text[:200]}
    except Exception as e:
        return {"error": str(e)}


# 3. ❌ Insecure Deserialization
@router.post("/deserialize")
def deserialize_data(data: str):
    decoded = base64.b64decode(data)
    obj = pickle.loads(decoded)  # DANGEROUS
    return {"result": str(obj)}


# 4. ❌ Debug info leak
@router.get("/debug")
def debug():
    import os
    return dict(os.environ)


# 5. ❌ Fake auth bypass
@router.get("/admin")
def admin(token: str = Query(None)):
    if token == "admin":
        return {"access": "granted"}
    return {"access": "denied"}
