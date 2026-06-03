from fastapi import APIRouter, Request

from slowapi import Limiter
from slowapi.util import get_remote_address

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)

limiter = Limiter(
    key_func=get_remote_address
)

@router.get("/")
@limiter.limit("5/minute")
async def health_check(request: Request):

    return {
        "status": "healthy"
    }