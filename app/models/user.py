from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id:Mapped[int] = mapped_column(
        Integer,
        Primary_key=True
    )
    email:Mapped[str] = mapped_column(
        String,
        unique=True,
        index=True
    )
    username:Mapped[str] = mapped_column(
        String,
        unique=True,
        index=True
    )
    password_hash:Mapped[str] = mapped_column(String)