""" User data model
"""

from sqlalchemy import Column, String, text, Boolean
from sqlalchemy.orm import relationship
from api.v1.models.base_model import BaseTableModel


class User(BaseTableModel):
    __tablename__ = "users"

    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    avatar_url = Column(String, nullable=True)
    is_active = Column(Boolean, server_default=text("true"))
    is_deleted = Column(Boolean, server_default=text("false"))
    is_verified = Column(Boolean, server_default=text("false"))

    token_login = relationship("TokenLogin", back_populates="user")
    subscription = relationship("UserSubscription", back_populates="user")