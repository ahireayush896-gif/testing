from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_todos_lifecycle():
    # Create todo
    response = client.post("/api/todos", json={
        "title": "Test Bee Detection",
        "description": "Test description",
        "completed": False,
        "priority": "high",
        "category": "Testing"
    })
    assert response.status_code == 201
    data = response.json()
    todo_id = data["id"]
    assert data["title"] == "Test Bee Detection"

    # Get todos
    response = client.get("/api/todos")
    assert response.status_code == 200
    todos = response.json()
    assert len(todos) >= 1
    assert isinstance(todos, list)

    # Get single todo
    response = client.get(f"/api/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json()["id"] == todo_id

    # Update todo
    response = client.put(f"/api/todos/{todo_id}", json={
        "completed": True
    })
    assert response.status_code == 200
    assert response.json()["completed"] is True

    # Delete todo
    response = client.delete(f"/api/todos/{todo_id}")
    assert response.status_code == 204
