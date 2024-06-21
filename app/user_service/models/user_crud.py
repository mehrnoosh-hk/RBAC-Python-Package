from sqlalchemy import select
from sqlalchemy.orm import Session

from app.user_service.schemas.user_schemas import UserCreate
from app.user_service.models.user_model import User
from app.user_service.schemas.user_schemas import User as PydanticUser


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


def get_user_by_id(session: Session, user_id: int) -> User | None:
    return session.get(User, user_id)


def get_all_users(session) -> list[PydanticUser]:
    statement = select(User)
    return [PydanticUser.model_validate(user) for user in session.scalars(statement).all()]
