import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app
from schemas import STaskAdd, STask

client = TestClient(app)

@pytest.mark.asyncio
@patch("repository.TaskRepository.find_all")  # Mocking the TaskRepository's find_all method
async def test_get_tasks(mock_find_all):
    # Mock the return value of the repository method
    mock_find_all.return_value = [
        STask(id=1, name="Test Task 1", description="Test task description 1"),
        STask(id=2, name="Test Task 2", description="Test task description 2"),
    ]

    response = client.get("/tasks")

    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 2
    assert tasks[0]["id"] == 1
    assert tasks[1]["name"] == "Test Task 2"

@pytest.mark.asyncio
@patch("repository.TaskRepository.add_one")  # Mocking the TaskRepository's add_one method
async def test_add_task(mock_add_one):
    # Mock the return value of the repository method
    mock_add_one.return_value = 123  # Simulating the task ID returned after insertion
    
    # Create the task with model_dump() and explicitly set description to None (optional field)
    task_data = STaskAdd(name="New Task", description=None)

    print("task_data")
    print(task_data)

    # Send the POST request, making sure it is sent as JSON in the body
    response = client.post("/tasks", json=task_data.model_dump())

    # Print response content for debugging
    if response.status_code != 200:
        print(f"Response Content: {response.text}")

    # Check if the status code is 200 (OK)
    assert response.status_code == 200
    result = response.json()
    assert result == {"ok": True, "task_id": 123}

