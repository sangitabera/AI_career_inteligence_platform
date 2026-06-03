from typing import List, Dict, ClassVar

from pydantic import BaseModel, Field
from pydantic import computed_field
from app.utils.normalizers import normalize_skills


class SalaryPredictionRequest(BaseModel):

    JobTitle: str = Field(alias="JobTitle")
    company_size: str
    company_industry: str
    country: str
    remote_type: str
    experience_level: str
    education_level: str
    posting_Year: int = Field(alias="posting_Year")
    years_experience: float
    Posting_Month : int = Field(alias='Posting Month')
    skills: List[str] = []
    hiring_urgency: str

    model_config = {
        "populate_by_name":True
    }


    # ----------------------------
    # COMPUTED FEATURES
    # ----------------------------
    industry_freq : ClassVar[Dict[str,int]] = {}
    @computed_field
    @property
    def industry_frequency(self) -> int:
        return self.industry_freq.get(self.company_industry, 0)
    
    
    job_freq : ClassVar[Dict[str,int]] = {}
    @computed_field
    @property
    def job_title_popularity(self) -> int:
        return self.job_freq.get(self.JobTitle, 0)
    

    @computed_field
    @property
    def total_skills(self) -> int:
        return len(self.skills)


    @computed_field
    @property
    def skills_python(self) -> int:
        return int("Python" in self.normalized_skills)


    @computed_field
    @property
    def skills_sql(self) -> int:
        return int("SQL" in self.normalized_skills)


    @computed_field
    @property
    def skills_ml(self) -> int:
        return int("ML" in self.normalized_skills)


    @computed_field
    @property
    def skills_deeplearning(self) -> int:
        return int("DeepLearning" in self.normalized_skills)


    @computed_field
    @property
    def skills_cloud(self) -> int:
        return int("Cloud" in self.normalized_skills)


    @computed_field
    @property
    def advanced_skill_score(self) -> int:

        score = 0

        if "Python" in self.normalized_skills:
            score += 2

        if "SQL" in self.normalized_skills:
            score += 2

        if "ML" in self.normalized_skills:
            score += 3

        if "DeepLearning" in self.normalized_skills:
            score += 4

        if "Cloud" in self.normalized_skills:
            score += 3

        return score


    @computed_field
    @property
    def ai_specialist(self) -> int:

        return int(
            "ML" in self.normalized_skills and
            "DeepLearning" in self.normalized_skills
        )


    @computed_field
    @property
    def exp_per_skill(self) -> float:

        if self.total_skills == 0:
            return 0.0

        return self.years_experience / self.total_skills


    @computed_field
    @property
    def experience_intensity(self) -> float:

        return (
            self.years_experience *
            self.advanced_skill_score
        )


    @computed_field
    @property
    def ml_cloud_combination(self) -> int:

        return int(
            "ML" in self.normalized_skills and
            "Cloud" in self.normalized_skills
        )


    @computed_field
    @property
    def premium_candidate(self) -> int:

        return int(
            self.advanced_skill_score >= 10 and
            self.years_experience >= 3
        )
    
    @computed_field
    @property
    def normalized_skills(self) -> str :
        return normalize_skills(
            self.skills
        )