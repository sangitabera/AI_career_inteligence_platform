from app.schemas.skill_gap_schema import SkillGapRequest
from app.ml.similarity_engine import analyze_skill_gap
from app.utils.normalizers import normalize_job_title, normalize_skills



def skill_gap_service(data: SkillGapRequest):
    normalized_role = normalize_job_title(data.target_role)
    normalized_skills = normalize_skills(data.skills)

    user_vector = [
        int("Python" in normalized_skills),
        int("SQL" in normalized_skills),
        int("ML" in normalized_skills),
        int("DeepLearning" in normalized_skills),
        int("Cloud" in normalized_skills)]

    result = analyze_skill_gap(
        user_vector = user_vector,
        target_role = normalized_role)

    return {
        "success": True,
        **result}