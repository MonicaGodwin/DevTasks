from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from app.database import Base
from sqlalchemy import DateTime, func, ForeignKey
from datetime import datetime

class Task(Base):
    __tablename__ = "tasks"
    id:Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )
    title:Mapped[str] = mapped_column(String)
    description:Mapped[str] = mapped_column(String)
    assigned_to:Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )
    status:Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )
    deadline:Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )
    created_by:Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )
    created_at:Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )
    