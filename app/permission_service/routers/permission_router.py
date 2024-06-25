from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.permission_service.schemas.permission_schemas import PermissionCreate, Permission
from app.permission_service.models.permission_crud import db_create_permission, db_get_all_permissions, db_get_permission_by_id
from app.core.database import get_session


permission_router = APIRouter(
    prefix="/permissions",
    tags=["permissions"]
)


@permission_router.get("/")
def get_all_permissions(session: Session = Depends(get_session)):
    return db_get_all_permissions(session)


@permission_router.post("/", response_model=Permission, status_code=status.HTTP_201_CREATED)
def create_new_permission(permission: PermissionCreate, session: Session = Depends(get_session)):
    try:
        return db_create_permission(permission, session)
    except ValueError:
        JSONResponse(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            content={"error": "Permission already exists"}
        )


@permission_router.get("/{permission_id}")
def get_permission_by_id(permission_id: int, session: Session = Depends(get_session)):
    return db_get_permission_by_id(permission_id, session)
