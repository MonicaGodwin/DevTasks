from pydantic import BaseModel, Field

class CreateUser(BaseModel):
    user_name: str = Field(min=2, max=20)
    email: str
    password: str

    