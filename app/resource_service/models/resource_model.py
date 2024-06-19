from sqlalchemy import UniqueConstraint, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Resource(Base):
    """
    Resource is a representation of a resource that can be accessed by a user.
    """

    __tablename__ = "resources"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
    description: Mapped[str]

    __table_args__ = (UniqueConstraint("name"),)
