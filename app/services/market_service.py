import pandas as pd
import joblib
from app.utils.cache import get_cache, set_cache

df = joblib.load(
    "data/artifacts/models/new_jobs_data.pkl"
)



SKILL_COLUMNS = [

    "Skills - Python",
    "Skills - SQL",
    "Skills - ML",
    "Skills-DeepLearning",
    "skills_Cloud"
]


# ---------------------------------------
# TRENDING SKILLS
# ---------------------------------------

def get_trending_skills():

    cached = get_cache("trending_skills")
    if cached:
        return cached
    
    skill_counts = {}

    for skill in SKILL_COLUMNS:
        skill_counts[skill] = int(df[skill].sum())

    sorted_skills = sorted(
        skill_counts.items(),
        key = lambda x: x[1],
        reverse=True
    )
    result = [
        {
            "skill": skill,
            "demand": count
        }
        for skill, count in sorted_skills
    ]
     
    set_cache(
        "trending_skills",
        result,
        expiry = 3600
    )
    return result


# ---------------------------------------
# TOP PAYING SKILLS
# ---------------------------------------

def get_top_paying_skills():

    results = []

    for skill in SKILL_COLUMNS:

        filtered = df[df[skill] == 1]

        avg_salary = round(

            filtered["Salary (USD)"].mean(),

            2
        )

        results.append({

            "skill": skill,
            "average_salary": avg_salary
        })

    results = sorted(

        results,

        key=lambda x: x["average_salary"],

        reverse=True
    )

    return results


# ---------------------------------------
# INDUSTRY DEMAND
# ---------------------------------------

def get_industry_demand():

    demand = (

        df["company_Industry"]

        .value_counts()

        .head(10)

        .to_dict()
    )

    return demand


# ---------------------------------------
# REMOTE WORK ANALYSIS
# ---------------------------------------

def get_remote_distribution():

    distribution = (

        df["Remote Type"]

        .value_counts()

        .to_dict()
    )

    return distribution


# ---------------------------------------
# EXPERIENCE VS SALARY
# ---------------------------------------

def get_experience_salary_analysis():

    grouped = (

        df.groupby("Years_Experience")

        ["Salary (USD)"]

        .mean()

        .reset_index()
    )

    grouped["Salary (USD)"] = grouped[
        "Salary (USD)"
    ].round(2)

    return grouped.to_dict(
        orient="records"
    )