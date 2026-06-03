from fastapi import APIRouter
from fastapi import Request

from slowapi import Limiter
from slowapi.util import get_remote_address

from app.schemas.recommendation_schema import (
    RecommendationRequest
)

from app.services.recommendation_service import (
    recommendation_service
)

router = APIRouter(
    prefix="/recommendation",
    tags=["Recommendation System"]
)

limiter = Limiter(
    key_func=get_remote_address
)


@router.post("/recommend")
@limiter.limit("5/minute")
async def recommend_jobs_api(
    request: Request,
    data: RecommendationRequest
):

    return recommendation_service(data)