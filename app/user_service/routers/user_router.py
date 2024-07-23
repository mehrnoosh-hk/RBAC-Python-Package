from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse

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
    try:
        user_crud.create_user(
            session=session,
            user=user)
        return {"username": user.username}
    except ValueError:
        return JSONResponse(
            content={"error": "A user with this email already exists"},
            status_code=status.HTTP_406_NOT_ACCEPTABLE
        )


@user_router.get("/")
async def get_all_users(session: Session = Depends(get_session)):
    return user_crud.get_all_users(session=session)


@user_router.get("/{user_id}")
async def get_user_by_id(user_id: int, session: Session = Depends(get_session)):
    return user_crud.get_user_by_id(
        session=session,
        user_id=user_id
    )
