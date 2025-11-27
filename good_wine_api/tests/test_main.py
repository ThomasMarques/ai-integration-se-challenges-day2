from fastapi.testclient import TestClient
from ..main import app
import json

# Initialize a FastAPI client
client = TestClient(app)


# Test your root endpoint
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello stranger! This API allow you to evaluate the quality of red wine. Go to the /docs for more details."
    }


# Test your predict endpoint
def test_predict():
    response = client.post(
        "/predict",
        headers={"accept": "application/json", "Content-Type": "application/json"},
        json={
            "alcohol": 9.4,
            "volatile_acidity": 0.7,
            "citric_acid": 0.0,
            "chlorides": 0.076,
            "density": 0.9978,
            "fixed_acidity": 7.3,
            "free_sulfur_dioxide": 11.0,
            "pH": 3.39,
            "residual_sugar": 1.6,
            "sulphates": 0.56,
            "total_sulfur_dioxide": 25.0,
        },
    )
    assert response.status_code == 200
    assert response.json() == json.dumps(
        {"prediction": 0, "probability": [0.7390607328281771, 0.260939267171823]}
    )
