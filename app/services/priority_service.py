from datetime import datetime, timezone, timedelta

now = datetime.now(timezone.utc)


task = {
    "id": 1,
    "title": "Fix login bug",
    "priority": "high",
    "status": "todo",
    "due_date": "2026-10-23T12:00:00+00:00"
}
def calculate_priority_score(task):
    if task['status'] == "completed":
        return 0
    
    score = 0
    if task['priority'] == "high":
        score = 30
    elif task['priority'] == "medium":
        score = 20
    else:
        score = 10

    return score


print(calculate_priority_score(task))

def calculate_deadline_score(task):
    if task['due_date'] is None:
        return 0
    deadline = datetime.fromisoformat(task['due_date'])
    now = datetime.now(timezone.utc)
    remaining_time =  deadline - now
    if remaining_time < timedelta(0):
        return 40
    if remaining_time <= timedelta(hours=24):
        return 30
    elif remaining_time <= timedelta(hours=72):
        return 20
    else:
        return 0
    

def calculate_task_urgency(task):
    if task['status'] == 'completed':
        return 0
    
    score1 = calculate_priority_score(task)
    score2 = calculate_deadline_score(task)
    total_urgency = score1 + score2
    return total_urgency

def rank_tasks(tasks):
    result = sorted(tasks, key=lambda task: calculate_task_urgency(task), reverse=True)
    return result

# task1 = {
#     "due_date": (now - timedelta(days=1)).isoformat()
# }

# task2 = {
#     "due_date": (now + timedelta(hours=12)).isoformat()
# }

# task3 = {
#     "due_date": (now + timedelta(days=2)).isoformat()
# }

# task4 = {
#     "due_date": (now + timedelta(days=7)).isoformat()
# }

# print(calculate_deadline_score(task1))
# print(calculate_deadline_score(task2))
# print(calculate_deadline_score(task3))
# print(calculate_deadline_score(task4))

task = {
    "id": 1,
    "title": "Fix login bug",
    "priority": "high",
    "status": "todo",
    "due_date": (
        datetime.now(timezone.utc) + timedelta(hours=12)
    ).isoformat()
}

print(calculate_task_urgency(task))