from fastapi import APIRouter
from fastapi_users import FastAPIUsers
from ..models import User
from ..auth import fastapi_users

router = APIRouter()

router.include_router(
    fastapi_users.get_register_router(User),
    prefix="",
)
router.include_router(
    fastapi_users.get_auth_router(),
    prefix="",
)
