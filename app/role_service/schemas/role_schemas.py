from pydantic import BaseModel


class RoleBase(BaseModel):
    name: str
    description: str


class RoleCreate(RoleBase):
    pass


class Role(RoleBase):
    id: int

    class Config:
        from_attributes = True