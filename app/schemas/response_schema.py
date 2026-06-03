from pydantic import BaseModel

class FeatureImpact(BaseModel):
    feature: str
    impact: float


class SalaryPredictionResponse(BaseModel):
    success: bool
    predicted_salary: float
    currency: str = "USD"
    top_feature_impacts: list[FeatureImpact] = []