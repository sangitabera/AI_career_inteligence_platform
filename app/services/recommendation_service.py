import joblib
import pandas as pd
from app.utils.cache import get_cache, set_cache
from sklearn.metrics.pairwise import cosine_similarity

from app.schemas.recommendation_schema import (
    RecommendationRequest
)


# ---------------------------------------
# LOAD ARTIFACTS
# ---------------------------------------

job_vectors = joblib.load(
    "data/vectorizers/new_job_skill_vectors.pkl"
)

tfidf_vectorizer = joblib.load(
    "data/vectorizers/new_tfidf_vectorizer.pkl"
)

jobs_df = joblib.load(
    "data/artifacts/models/new_jobs_data.pkl"
)


# ---------------------------------------
# RECOMMENDATION ENGINE
# ---------------------------------------

def recommendation_service(
    data: RecommendationRequest
):

    # Create unique cache key
    cache_key = f"recommend:{'-'.join(sorted(data.skills))}:{data.top_k}"

    # Try cache first
    cached = get_cache(cache_key)

    if cached:
        return cached

    # Convert skills into text
    user_text = " ".join(data.skills)

    # Vector transformation
    user_vector = tfidf_vectorizer.transform(
        [user_text]
    )

    # Cosine similarity
    similarities = cosine_similarity(
        user_vector,
        job_vectors
    )[0]

    # Get top indices
    top_indices = similarities.argsort()[
        ::-1
    ][:data.top_k]

    recommendations = []
    seen_roles = set()

    for idx in top_indices:

        role = jobs_df.iloc[idx]["JobTitle"]

        # Avoid duplicate roles
        if role in seen_roles:
            continue

        seen_roles.add(role)

        score = round(
            similarities[idx] * 100,
            2
        )

        recommendations.append({
            "job_role": role,
            "match_score": score
        })

    result = {
        "success": True,
        "recommendations": recommendations
    }

    # Save result to cache
    set_cache(cache_key, result, expiry=3600)

    return result