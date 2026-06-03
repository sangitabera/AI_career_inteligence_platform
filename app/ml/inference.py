import pandas as pd
from app.utils.logger import logger
from app.schemas.salary_schema import SalaryPredictionRequest
from app.ml.model_loader import salary_model
import numpy as np
from app.utils.normalizers import (
    normalize_company_size,
    normalize_education_level,
    normalize_experience_level,
    normalize_job_title,
    normalize_industry,
    normalize_remote_type,
    normalize_skills
)




def predict_salary(data):

    skills = [skill.lower() for skill in data["skills"]]
    total_skills = len(skills)
    has_ml = int("ml" in skills)
    has_python = int("python" in skills)
    has_sql = int("sql" in skills)
    has_cloud = int(
        "aws" in skills or
        "azure" in skills or
        "gcp" in skills)
    has_dl = int(
        "deep learning" in skills or
        "deeplearning" in skills)

    advanced_skill_score = (
        has_python +
        has_sql +
        has_ml +
        has_cloud +
        has_dl
    )

    ml_cloud_combination = int(
        has_ml and has_cloud
    )

    ai_specialist = int(
        has_ml or has_dl
    )

    premium_candidate = int(
        advanced_skill_score >= 3 and
        data["years_experience"] >= 2
    )

    exp_per_skill = (
        data["years_experience"] /
        max(total_skills, 1)
    )

    experience_intensity = (
        data["years_experience"] *
        advanced_skill_score
    )

    job_title_popularity = 1

    industry_frequency = 1

    input_data = {

        "Remote Type":
            str(data["remote_type"]),

        "advanced_skill_score":
            advanced_skill_score,

        'JobTitle':
            str(data["JobTitle"]),

        'posting_Year':
            int(data["posting_Year"]),

        "Posting Month": 
            int(data["Posting_Month"]),

        # =========================
        # SKILL FEATURES
        # =========================

        "Skills - Python":
            int("python" in skills),

        "Skills - SQL":
            int("sql" in skills),

        "Skills - ML":
            int(
                "ml" in skills or
                "machine learning" in skills
            ),

        "Skills-DeepLearning":
            int(
                "deep learning" in skills or
                "deeplearning" in skills
            ),

        "skills_Cloud":
            int(
                "aws" in skills or
                "azure" in skills or
                "gcp" in skills
            ),

        "exp_per_skill":
            exp_per_skill,

        "job_title_popularity":
            job_title_popularity,

        "experience_intensity":
            experience_intensity,

        'Education  Level':
            str(data["education_level"]),

        'Exp. Level':
            str(data["experience_level"]),

        "ml_cloud_combination":
            ml_cloud_combination,

        "premium_candidate":
            premium_candidate,

        "Hiring Urgency":
            data["hiring_urgency"],

        "Country":
            str(data["country"]),

        "industry_frequency":
            industry_frequency,

        "Company Size":
            str(data["company_size"]),

        'company_Industry':
            str(data["company_industry"]),

        "Total_Skills":
            int(data['total_skills']),

        "ai_specialist":
            ai_specialist,

        'Years_Experience':
            int(data["years_experience"])
    }

    logger.info(f"Prediction input: {input_data}")
    df = pd.DataFrame([input_data])

   
    # Remove unsupported columns
    df = df.drop(
        columns=["skills", "normalized_skills"],
        errors="ignore"
    )

    categorical_columns = [
    "JobTitle",
    "Company Size",
    "company_Industry",
    "Country",
    "Remote Type",
    "Exp. Level",
    'Hiring Urgency',
    "Education  Level"]

    for col in categorical_columns:
         df[col] = df[col].astype(str)

    numeric_columns = [

    "posting_Year",
    "Posting Month",
    "Years_Experience",
    "Skills - Python",
    "Skills - SQL",
    "Skills - ML",
    "Skills-DeepLearning",
    "skills_Cloud",
    "Total_Skills",
    "advanced_skill_score",
    "ml_cloud_combination",
    "premium_candidate",
    "exp_per_skill",
    "job_title_popularity",
    "industry_frequency",
    "experience_intensity",
    "ai_specialist"]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col])
    
    df = pd.DataFrame([input_data])
        
    prediction = salary_model.predict(df)[0]
    prediction = np.expm1(prediction)
    logger.info(f"Prediction output: {prediction}")
    return round(float(prediction), 2)