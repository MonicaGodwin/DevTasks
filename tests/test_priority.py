import pytest
from app.services.priority_service import calculate_task_urgency, rank_tasks
from datetime import datetime, timezone, timedelta

def test_low_priority_task():
    task = {
        "id": 1,
        "title": "Update README",
        "priority": "low",
        "status": "todo",
        "due_date": None
    }

    # Call your calculate_task_urgency function
    result = calculate_task_urgency(task)

    # Use assert to verify the result
    assert result == 10

def test_completed_task():
    task = {
        "id": 2,
        "title": "Database setup",
        "priority": "high",
        "status": "completed",
        "due_date": None
    }

    result = calculate_task_urgency(task)
    assert result == 0

# Get the current UTC time using datetime.now(timezone.utc).
# Subtract one day using timedelta(days=1).
# Convert the result to a string using .isoformat().
# Create a task dictionary with that string as its due_date.
# Call calculate_task_urgency(task).
# Use assert to verify that the result equals 70.
def test_overdue_task():
    current_time = datetime.now(timezone.utc)
    yesterday = current_time - timedelta(days=1)    
    task = {
        "id": 2,
        "title": "Database setup",
        "priority": "high",
        "status": "todo",
        "due_date": yesterday.isoformat()
    }

    result = calculate_task_urgency(task)
    assert result == 70


def test_rank_tasks():
    now = datetime.now(timezone.utc)

    tasks = [
        {
            "id": 1,
            "priority": "low",
            "status": "todo",
            "due_date": None
        },
        {
            "id": 2,
            "priority": "high",
            "status": "todo",
            "due_date": (now - timedelta(days=1)).isoformat()
        },
        {
            "id": 3,
            "priority": "medium",
            "status": "todo",
            "due_date": None
        }
    ]

    ranked_tasks = rank_tasks(tasks)

    # Write your assertions here
    assert ranked_tasks[0]["id"] == 2
    assert ranked_tasks[1]["id"] == 3
    assert ranked_tasks[2]["id"] == 1