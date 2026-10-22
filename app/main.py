from fastapi import FastAPI
from app.models.user import User
from app.models.task import Task
from app.database import create_tables

app = FastAPI(
    title="DevTasks",
    description="Task management API",
    version="1.0.0"
)

create_tables()

@app.get("/")
def home():
    return {"Welcome to dev tasks"}