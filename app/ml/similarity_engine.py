import joblib
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity


role_profiles = joblib.load(
    "data/artifacts/models/role_job_profiles.pkl"
)


SKILL_COLUMNS = [

    "Skills - Python",
    "Skills - SQL",
    "Skills - ML",
    "Skills-DeepLearning",
    "skills_Cloud"
]


def analyze_skill_gap(
    user_vector,
    target_role
):

    role_data = role_profiles.loc[target_role]

    role_vector = role_data[SKILL_COLUMNS].values.reshape(1, -1)

    similarity = cosine_similarity(
        [user_vector],
        role_vector
    )[0][0]

    missing_skills = []

    for idx, skill in enumerate(SKILL_COLUMNS):

        required = role_vector[0][idx]

        current = user_vector[idx]

        if required >= 0.5 and current == 0:

            missing_skills.append(skill)

    match_percentage = round(similarity * 100, 2)

    return {
        "match_percentage": match_percentage,
        "missing_skills": missing_skills
    }