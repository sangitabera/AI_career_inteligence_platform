from typing import List
from pydantic import BaseModel

class RecommendationRequest(BaseModel):
    skills : List[str]
    top_k: int = 5