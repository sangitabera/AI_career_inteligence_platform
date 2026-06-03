from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_salary_prediction():

    payload = {

        "job_title": "ML Engineer",
        "company_size": "Medium",
        "company_industry": "Technology",
        "country": "India",
        "remote_type": "Hybrid",
        "experience_level": "Mid",
        "education_level": "Bachelor",
        "Posting_month":3,
        "Posting_year":2025,

        "years_experience": 3,

        "skills": [
            "Python",
            "SQL",
            "ML",
            "Cloud"
        ],

        "hiring_urgency": 2
    }

    response = client.post(
        "/salary/predict",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert "predicted_salary" in data