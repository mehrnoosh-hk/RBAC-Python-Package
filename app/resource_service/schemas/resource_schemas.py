from pydantic import BaseModel


class ResourceBase(BaseModel):
    name: str
    description: str


class Resource(ResourceBase):
    id: int

    class Config:
        from_attributes = True
