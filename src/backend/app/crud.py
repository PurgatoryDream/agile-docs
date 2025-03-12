from sqlalchemy.orm import Session
from uuid import UUID
import uuid

from .routers.auth import get_password_hash
from . import dbmodels, schemas

def get_user(db: Session, username: str) -> dbmodels.User:
    return db.query(dbmodels.User).filter(dbmodels.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    id_user = uuid.uuid4()
    hashed_password = get_password_hash(user.password)
    db_user = dbmodels.User(id=id_user, username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_repository(db: Session, repository_id: UUID) -> dbmodels.Repository:
    return db.query(dbmodels.Repository).filter(dbmodels.Repository.id == repository_id).first()

def get_user_repositories(db: Session, username: str):
    db_user = get_user(db, username)
    return db.query(dbmodels.UserPermission).filter(dbmodels.UserPermission.user_id == db_user.id).all()

def create_new_repo(db: Session, username: str, repo: schemas.RepositoryCreate):
    id_repo = uuid.uuid4()
    db_repo = dbmodels.Repository(id=id_repo, name=repo.name)
    db.add(db_repo)
    db.commit()
    db.refresh(db_repo)
    
	# Find the user:
    db_user = get_user(db, username)
    
	# Update the user permissions table:
    db_user_perms = dbmodels.UserPermission(user_id=db_user.id, repository_id=id_repo, permission_level="owner")
    db.add(db_user_perms)
    db.commit()
    db.refresh(db_user_perms)
    return db_repo, db_user_perms
