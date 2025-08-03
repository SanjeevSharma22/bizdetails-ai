from fastapi import APIRouter

router = APIRouter()


@router.post("/credits/assign")
def assign_credits():
    return {"status": "ok"}


@router.get("/users")
def list_users():
    return []


@router.post("/users/{user_id}/role")
def change_role(user_id: int):
    return {"user_id": user_id, "role": "user"}
