from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_items():
    response = client.post("/api/add", json={"numbers": [1, 2, 3, 4]})
    assert response.status_code == 200
    assert response.json() == {"result": 10}

def test_add_empty_list():
    response = client.post("/api/add", json={"numbers": []})
    assert response.status_code == 200
    assert response.json() == {"result": 0}

def test_add_negative_numbers():
    response = client.post("/api/add", json={"numbers": [-1, -2, -3, -4]})
    assert response.status_code == 200
    assert response.json() == {"result": -10}
