import datetime

from sqlalchemy import TIMESTAMP, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Resource(Base):
    """
    Resource is a representation of a resource that can be accessed by a user.
    """

    __tablename__ = "resources"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    description: Mapped[str]
    created_at: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP(timezone=True), default=datetime.datetime.now, nullable=True
    )

    __table_args__ = (UniqueConstraint("name"),)
