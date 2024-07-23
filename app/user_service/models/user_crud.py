from sqlalchemy import select
from sqlalchemy.orm import Session

from app.user_service.schemas.user_schemas import UserCreate
from app.user_service.models.user_model import User
from app.user_service.schemas.user_schemas import User as PydanticUser
from app.auth_service.security import get_password_hash


def create_user(session: Session, user: UserCreate) -> User:
    #  First check that if a user with this email exists or not
    existing_user = session.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise ValueError("A user with this email already exists")
    
    db_user: User = User(
        email=user.email,
        username=user.username,
        password=get_password_hash(user.password),
        enabled=user.enabled
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
