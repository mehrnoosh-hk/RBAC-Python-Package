from sqlalchemy.orm import Session

from app.role_service.models.role_model import Role
from app.role_service.schemas.role_schemas import RoleCreate
from app.role_service.schemas.role_schemas import Role as PydanticRole


def create_role(session: Session, role: RoleCreate) -> PydanticRole:
    # Check if role already exists
    db_role = session.query(Role).filter(Role.name == role.name).first()
    if db_role:
        raise ValueError("Role already exists")
    db_role = Role(
        name=role.name,
        description=role.description
    )
    session.add(db_role)
    session.commit()
    session.refresh(db_role)
    return PydanticRole.model_validate(db_role)

def get_all_roles(session: Session) -> list[PydanticRole]:
    roles = session.query(Role).all()
    return [PydanticRole.model_validate(role) for role in roles]
