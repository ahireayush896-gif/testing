from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_todos_endpoints():
    response = client.get("/api/todos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
