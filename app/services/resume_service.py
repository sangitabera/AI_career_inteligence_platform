import joblib
import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity

from app.utils.resume_parser import (
    extract_resume_text
)

from app.utils.text_cleaner import (
    clean_text
)

from app.ml.similarity_engine import (
    analyze_skill_gap
)


# -----------------------------------
# LOAD ARTIFACTS
# -----------------------------------

tfidf_vectorizer = joblib.load(
    "data/vectorizers/new_tfidf_vectorizer.pkl"
)

job_vectors = joblib.load(
    "data/vectorizers/new_job_skill_vectors.pkl"
)

jobs_df = joblib.load(
    "data/artifacts/models/new_jobs_data.pkl"
)


# SKILL DATABASE

KNOWN_SKILLS = [

    "python",
    "sql",
    "machine learning",
    "deep learning",
    "cloud",
    "tensorflow",
    "pytorch",
    "data analysis"
]


# -----------------------------------
# RESUME ANALYZER
# -----------------------------------

def resume_analysis_service(
    file_path: str
):

    # ----------------------------
    # Extract Text
    # ----------------------------

    text = extract_resume_text(file_path)

    cleaned_text = clean_text(text)


    # ----------------------------
    # Extract Skills
    # ----------------------------

    extracted_skills = []

    for skill in KNOWN_SKILLS:

        if skill in cleaned_text:

            extracted_skills.append(skill)


    # ----------------------------
    # Vectorization
    # ----------------------------

    resume_vector = tfidf_vectorizer.transform(
        [" ".join(extracted_skills)]
    )


    # ----------------------------
    # Similarity
    # ----------------------------

    similarities = cosine_similarity(
        resume_vector,
        job_vectors
    )[0]

    best_idx = similarities.argmax()

    recommended_role = jobs_df.iloc[
        best_idx
    ]["JobTitle"]

    ats_score = round(
        similarities[best_idx] * 100,
        2
    )


    # ----------------------------
    # Skill Gap
    # ----------------------------

    normalized_skills = []

    if "python" in extracted_skills:
        normalized_skills.append("Python")

    if "sql" in extracted_skills:
        normalized_skills.append("SQL")

    if "machine learning" in extracted_skills:
        normalized_skills.append("ML")

    if "deep learning" in extracted_skills:
        normalized_skills.append("DeepLearning")

    if "cloud" in extracted_skills:
        normalized_skills.append("Cloud")


    user_vector = [

        int("Python" in normalized_skills),
        int("SQL" in normalized_skills),
        int("ML" in normalized_skills),
        int("DeepLearning" in normalized_skills),
        int("Cloud" in normalized_skills)
    ]


    gap_result = analyze_skill_gap(
        user_vector=user_vector,
        target_role=recommended_role
    )


    return {

        "success": True,

        "ats_score": ats_score,

        "extracted_skills": extracted_skills,

        "recommended_role": recommended_role,

        "missing_skills": gap_result[
            "missing_skills"
        ]
    }