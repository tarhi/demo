import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from app.services.database import Base


class User(Base):
    _tablename_ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True,nullable=False)
    full_name = Column(String, index=True)
    username = Column(String, unique=True, index=True, nullable=True)
    password = Column(String, nullable=True)