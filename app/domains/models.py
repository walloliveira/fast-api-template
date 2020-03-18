from uuid import uuid4

from sqlalchemy import String, Column

from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid4()))
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
