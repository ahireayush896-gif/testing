from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from datetime import datetime

from backend.models import TodoItem, TodoCreate, TodoUpdate

app = FastAPI(
    title="To-Do List API",
    description="A robust FastAPI backend for managing to-do list items with categories, priorities, and persistence.",
    version="1.0.0"
)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage for demonstration (can be replaced with a database later)
fake_todos_db = []
counter = 0

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the To-Do List API!", "docs": "/docs"}

@app.get("/api/todos", response_model=List[TodoItem], tags=["Todos"])
def get_todos(completed: Optional[bool] = None, priority: Optional[str] = None):
    results = fake_todos_db
    if completed is not None:
        results = [t for t in results if t["completed"] == completed]
    if priority is not None:
        results = [t for t in results if t["priority"].lower() == priority.lower()]
    return results

@app.post("/api/todos", response_model=TodoItem, status_code=status.HTTP_201_CREATED, tags=["Todos"])
def create_todo(todo: TodoCreate):
    global counter
    counter += 1
    now = datetime.utcnow()
    new_item = {
        "id": counter,
        "title": todo.title,
        "description": todo.description,
        "completed": todo.completed,
        "priority": todo.priority,
        "category": todo.category,
        "created_at": now,
        "updated_at": now
    }
    fake_todos_db.append(new_item)
    return new_item

@app.get("/api/todos/{todo_id}", response_model=TodoItem, tags=["Todos"])
def get_todo(todo_id: int):
    for todo in fake_todos_db:
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo item with id {todo_id} not found")

@app.put("/api/todos/{todo_id}", response_model=TodoItem, tags=["Todos"])
def update_todo(todo_id: int, todo_update: TodoUpdate):
    for index, todo in enumerate(fake_todos_db):
        if todo["id"] == todo_id:
            update_data = todo_update.dict(exclude_unset=True)
            updated_item = {**todo, **update_data, "updated_at": datetime.utcnow()}
            fake_todos_db[index] = updated_item
            return updated_item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo item with id {todo_id} not found")

@app.delete("/api/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Todos"])
def delete_todo(todo_id: int):
    for index, todo in enumerate(fake_todos_db):
        if todo["id"] == todo_id:
            fake_todos_db.pop(index)
            return None
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo item with id {todo_id} not found")
