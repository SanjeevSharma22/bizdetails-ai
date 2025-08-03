from fastapi import APIRouter

router = APIRouter()


@router.get("/usage")
def credit_usage():
    return {"used": 0}


@router.get("/allocated")
def credit_allocated():
    return {"allocated": 0}


@router.get("/reports/dashboard")
def dashboard():
    return {"credits_used": 0, "credits_allocated": 0}
