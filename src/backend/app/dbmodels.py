import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

BaseDB = declarative_base()

class User(BaseDB):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String(length=255), nullable=False)
    
class Repository(BaseDB):
    __tablename__ = "repositories"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    description = Column(String)
    
class UserPermission(BaseDB):
    __tablename__ = "userpermissions"
    
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), primary_key=True)
    repository_id = Column(UUID(as_uuid=True), ForeignKey('repositories.id'), primary_key=True)
    permission_level = Column(String)
