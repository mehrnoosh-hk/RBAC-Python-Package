from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

import app.role_service.models.role_crud as role_crud
from app.core.database import get_session
from app.role_service.schemas.role_schemas import RoleCreate, Role

role_router = APIRouter(prefix="/roles", tags=["roles"])


@role_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Role)
def create_role(role: RoleCreate, session: Session = Depends(get_session)) -> Role | JSONResponse:
    try:
        new_role = role_crud.create_role(session=session, role=role)
        return new_role
    except ValueError:
        return JSONResponse(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            content={"error": "Role already exists"},
        )
    

@role_router.get("/", response_model=list[Role])
def get_all_roles(session: Session = Depends(get_session)) -> list:
    return role_crud.get_all_roles(session=session)


@role_router.post("/{user_id}")
def assign_role_to_user(user_id: int, role_id: int) -> dict:
    return {"role_id": role_id}
