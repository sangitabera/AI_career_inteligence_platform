from fastapi import APIRouter
from fastapi import Request

from slowapi.util import get_remote_address
from slowapi import Limiter

from app.schemas.salary_schema import SalaryPredictionRequest
from app.schemas.response_schema import SalaryPredictionResponse

from app.services.salary_service import salary_prediction_service

router = APIRouter(
    prefix="/salary",
    tags=["Salary Prediction"]
)

limiter = Limiter(
    key_func=get_remote_address
)


@router.post(
    "/predict",
    response_model=SalaryPredictionResponse
)
@limiter.limit("5/minute")
async def predict_salary_api(
    request: Request,
    data: SalaryPredictionRequest):

    result = salary_prediction_service(data.dict())

    return result