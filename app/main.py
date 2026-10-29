from fastapi import FastAPI, Depends
from app.models.user import User
from app.models.task import Task
from app.database import create_tables, get_database
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.schemas.user import CreateUser
from pwdlib import PasswordHash

app = FastAPI(
    title="DevTasks",
    description="Task management API",
    version="1.0.0"
)

create_tables()

@app.get("/")
def home():
    return {"Welcome to dev tasks"}

@app.get("/users")
def get_users(db: Session = Depends(get_database)):
    statement = select(User)
    result = db.execute(statement)
    users = result.scalars().all()
    return users

@app.post("/register_user")
def register_user(user: CreateUser):
    password_hash = PasswordHash.recommended()