import joblib

from app.utils.logger import logger

MODEL_PATH = "data/artifacts/models/new_salary_prediction_pipeline.pkl"

try:
    salary_model = joblib.load(MODEL_PATH)
    logger.info("Salary prediction pipeline loaded successfully")
except Exception as e:
    logger.error(f"Error loading model: {e}")
    salary_model = None