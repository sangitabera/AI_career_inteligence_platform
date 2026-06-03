from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_recommendation_system():

    payload = {

        "skills": [
            "Python",
            "Machine Learning",
            "SQL"
        ],

        "top_k": 5
    }

    response = client.post(

        "/recommendation/recommend",

        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert "recommendations" in data