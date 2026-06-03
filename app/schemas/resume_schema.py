from pydantic import BaseModel

class ResumeAnalysisResponse(BaseModel):
    success: bool
    ats_score: float
    extracted_skills: list
    recommended_role: str
    missing_skills: list
