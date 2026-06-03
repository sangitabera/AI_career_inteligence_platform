from typing import List

from pydantic import BaseModel
from pydantic import computed_field


class SkillGapRequest(BaseModel):
    target_role: str
    skills: List[str]

    @computed_field
    @property
    def skills_python(self) -> int:
        return int("Python" in self.skills)


    @computed_field
    @property
    def skills_sql(self) -> int:
        return int("SQL" in self.skills)


    @computed_field
    @property
    def skills_ml(self) -> int:
        return int("ML" in self.skills)


    @computed_field
    @property
    def skills_deeplearning(self) -> int:
        return int("DeepLearning" in self.skills)


    @computed_field
    @property
    def skills_cloud(self) -> int:
        return int("Cloud" in self.skills)