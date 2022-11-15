import string
from typing import List, Union

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True


class ServiceBase(BaseModel):
    name: str
    description: str
    status: str
    stage: str
    documentation_link: str
    version: str
    instance: int
    created_at: str
    updated_at: str
    # configuration: str


class Service(ServiceBase):
    id: int
    # name: str

    class Config:
        orm_mode = True


class ServiceCreate(ServiceBase):
    pass
