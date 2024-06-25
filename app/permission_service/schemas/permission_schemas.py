from pydantic import BaseModel


class PermissionBase(BaseModel):
    name: str
    description: str


class PermissionCreate(PermissionBase):
    pass


class Permission(PermissionBase):
    id: int

    class Config:
        from_attributes = True
