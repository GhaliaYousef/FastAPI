from xmlrpc.client import DateTime
from django.forms import JSONField
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")


class Services(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    name =Column(String, index=True)
    description = Column(String, index=True)
    instance = Column(Integer, index=True)
    # configuration = Column(String, index=True)
    status = Column(String, index=True, default="ACTIVE")
    stage = Column(String, index=True, default="DEV")
    documentation_link = Column(String, index=True, default="")
    version = Column(String, default="1.0.0", index=True)
    # logo = Column(String,default="", index=True)
    created_at = Column(String, index=True)
    updated_at = Column(String, index=True)

    # owner = relationship("User", back_populates="services")