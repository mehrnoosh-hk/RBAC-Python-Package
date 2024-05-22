from typing import Type

from sqlmodel import Session, select

from app.user_service.schemas.user_schemas import UserCreate
from app.user_service.models.user_model import User


def create_user(session: Session, user: UserCreate) -> User:
    db_user: User = User(
        email=user.email,
        username=user.username,
        password=user.password
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def get_user_by_id(session: Session, user_id: int) -> Type[User] | None:
    user = session.get(User, user_id)
    return user


def get_all_users(session) -> list[Type[User]]:
    statement = select(User)
    users = session.exec(statement).all()
    return users
