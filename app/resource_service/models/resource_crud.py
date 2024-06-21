from sqlalchemy.orm import Session

from app.resource_service.schemas.resource_schemas import ResourceCreate
from app.resource_service.models.resource_model import Resource


def db_create_resource(resource: ResourceCreate, session: Session) -> Resource:
    # Check if the resource already exist
    existing_resource = session.query(Resource).filter(Resource.name == resource.name).first()
    if existing_resource:
        raise ValueError("Resource already exists")
    new_resource: Resource = Resource(
        **resource.model_dump()
    )
    session.add(new_resource)
    session.commit()
    session.refresh(new_resource)

    return new_resource


def db_get_all_resources(session: Session) -> list[Resource]:
    return session.query(Resource).all()
