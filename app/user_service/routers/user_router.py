from fastapi import APIRouter, status, Depends

from sqlmodel import Session

from app.user_service.schemas.user_schemas import UserCreate
from app.user_service.models import user_crud
from app.core.database import get_session

user_router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@user_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, session: Session = Depends(get_session)):
    user_crud.create_user(
        session=session,
        user=user)
    return {"username": user.username}


@user_router.get("/")
async def get_all_users(session: Session = Depends(get_session)):
    users = user_crud.get_all_users(session=session)
    return users


@user_router.get("/{user_id}")
async def get_user_by_id(user_id: int, session: Session = Depends(get_session)):
    user = user_crud.get_user_by_id(
        session=session,
        user_id=user_id
    )
    return user
