from fastapi import FastAPI
from app.routes import vulnerable, safe

app = FastAPI(title="Vulnerable MCP Lab ⚠️")

app.include_router(vulnerable.router, prefix="/vuln", tags=["Vulnerable"])
app.include_router(safe.router, prefix="/safe", tags=["Safe"])

@app.get("/")
def root():
    return {"message": "Vulnerable MCP Lab Running ⚠️"}
