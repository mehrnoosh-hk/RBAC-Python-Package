import datetime
from typing import Optional

from pydantic import BaseModel


class ResourceBase(BaseModel):
    name: str
    description: str
    created_at: Optional[datetime.datetime] = None


class ResourceCreate(ResourceBase): ...


class Resource(ResourceBase):
    id: int

    class Config:
        from_attributes = True
