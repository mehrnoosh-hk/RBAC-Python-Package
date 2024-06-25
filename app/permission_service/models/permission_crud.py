from sqlalchemy.orm import Session

from app.permission_service.schemas.permission_schemas import PermissionCreate
from app.permission_service.schemas.permission_schemas import Permission as PydanticPermission
from app.permission_service.models.permission_model import Permission


def db_create_permission(permission: PermissionCreate, session: Session) -> PydanticPermission:
    # Check if that permission already exist
    existing_permission = session.query(Permission).filter(Permission.name == permission.name).first()
    if existing_permission:
        raise ValueError("Permission already exists")
    db_permission: Permission = Permission(
        **permission.model_dump()
    )
    session.add(db_permission)
    session.commit()
    session.refresh(db_permission)

    return PydanticPermission.model_validate(db_permission)


def db_get_all_permissions(session: Session) -> list[PydanticPermission]:
    permissions = session.query(Permission).all()
    return [PydanticPermission.model_validate(permission) for permission in permissions]


def db_get_permission_by_id(permission_id: int, session: Session) -> PydanticPermission:
    permission = session.query(Permission).filter(Permission.id == permission_id).first()
    return PydanticPermission.model_validate(permission)
