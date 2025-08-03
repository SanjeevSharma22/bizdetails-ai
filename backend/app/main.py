from fastapi import FastAPI
from .routers import auth, companies, enrich, credits, admin

app = FastAPI(title="BizDetails AI")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(companies.router, prefix="/companies", tags=["companies"])
app.include_router(enrich.router, prefix="/enrich", tags=["enrich"])
app.include_router(credits.router, prefix="/credits", tags=["credits"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])


@app.get("/")
def read_root():
    return {"status": "ok"}
