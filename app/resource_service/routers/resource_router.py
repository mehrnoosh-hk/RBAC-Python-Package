from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.resource_service.schemas.resource_schemas import ResourceCreate, Resource
from app.resource_service.models.resource_crud import db_create_resource, db_get_all_resources
from app.core.database import get_session


resource_router = APIRouter(
    prefix="/resources",
    tags=["resources"],
)


@resource_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Resource)
def create_resource(
    resource: ResourceCreate, session: Session = Depends(get_session)
):
    try:
        return db_create_resource(resource=resource, session=session)
    except ValueError:
        return JSONResponse(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            content={"error": "Resource already exists"},
        )


@resource_router.get("/", status_code=status.HTTP_200_OK)
def get_all_resources(session: Session = Depends(get_session)):
    return db_get_all_resources(session)