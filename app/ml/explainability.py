import shap
import pandas as pd
import joblib


model_pipeline = joblib.load("data/artifacts/models/new_salary_prediction_pipeline.pkl")

model = model_pipeline.named_steps["model"]
preprocessor = model_pipeline.named_steps["preprocessor"]
explainer = shap.Explainer(model)

def explain_prediction(input_df: pd.DataFrame):
    print(input_df.columns.tolist())
    print(input_df.dtypes)
    print(input_df.iloc[0].to_dict())

    transformed = preprocessor.transform(input_df)
    shap_values = explainer(transformed)
    feature_names = preprocessor.get_feature_names_out()
    contributions = []

    for idx, value in enumerate(shap_values.values[0]):
        contributions.append({
            "feature": feature_names[idx],
            "impact": round(float(value), 4)
        })

    contributions = sorted(contributions, key=lambda x: abs(x["impact"]), reverse=True)
    return contributions[:10]

