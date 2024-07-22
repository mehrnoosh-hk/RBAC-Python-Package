import datetime

from sqlalchemy import Integer, String, Boolean, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    username: Mapped[str]
    password: Mapped[str]
    enabled: Mapped[bool] = mapped_column(Boolean, nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP(timezone=True), default=datetime.datetime.now, nullable=True
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP(timezone=True), default=datetime.datetime.now, nullable=True
    )
    deleted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=True)
    deleted_at: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP(timezone=True), nullable=True
    )
