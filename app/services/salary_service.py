import pandas as pd
from app.schemas.salary_schema import SalaryPredictionRequest
from app.ml.inference import predict_salary
from app.ml.explainability import explain_prediction
from app.utils.logger import logger


def salary_prediction_service(data: SalaryPredictionRequest):
    logger.info(
        f"Salary Prediction Request: {data}"
    )
    prediction = predict_salary(data)


    input_df = pd.DataFrame([{

        "JobTitle": data["JobTitle"],

        "Company Size": data["company_size"],

        "company_Industry":
            data["company_industry"],

        "Country": data["country"],

        "Remote Type": data["remote_type"],

        "Exp. Level":
            data["experience_level"],

        "Years_Experience":
            data["years_experience"],

        "Education  Level":
            data["education_level"],

        "Posting Month":
            data["Posting_Month"],

        "posting_Year":
            data["posting_Year"],

        "Hiring Urgency":
            data["hiring_urgency"],

        "Total_Skills":
            data["total_skills"],

        "advanced_skill_score":
            data["advanced_skill_score"],

        "ai_specialist":
            data["ai_specialist"],

        "exp_per_skill":
            data["exp_per_skill"],

        "experience_intensity":
            data["experience_intensity"],

        "ml_cloud_combination":
            data["ml_cloud_combination"],

        "premium_candidate":
            data["premium_candidate"],

        "Skills - Python":
            data["skills_python"],

        "Skills - SQL":
            data["skills_sql"],

        "Skills - ML":
            data["skills_ml"],

        "Skills-DeepLearning":
            data["skills_deeplearning"],

        "skills_Cloud":
            data["skills_cloud"],
        
        "job_title_popularity":
            data["job_title_popularity"],

        "industry_frequency":
            data["industry_frequency"]
    }])


    explanations = explain_prediction(input_df)
    logger.info(f"Prediction: {prediction}")

    return {
        "success": True,
        "predicted_salary": prediction,
        "top_feature_impacts":
            explanations
    }