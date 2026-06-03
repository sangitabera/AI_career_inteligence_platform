from fastapi import APIRouter
from fastapi import Request

from slowapi import Limiter
from slowapi.util import get_remote_address

from app.schemas.skill_gap_schema import (
    SkillGapRequest
)

from app.services.skill_gap_service import (
    skill_gap_service
)

router = APIRouter(
    prefix="/skill-gap",
    tags=["Skill Gap"]
)

limiter = Limiter(
    key_func=get_remote_address
)


@router.post("/analyze")
@limiter.limit("5/minute")
async def analyze_skill_gap_api(
    request: Request,
    data: SkillGapRequest
):

    return skill_gap_service(data)