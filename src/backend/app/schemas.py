from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID

###########################################################
######### Auth Classes                
########################################################### 
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: str | None = None
    
###########################################################
######### User Classes                
########################################################### 
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class User(BaseModel):
    id: UUID
    username: str
    email: str
    
class UserDB(User):
    hashed_password: str

###########################################################
######### Repository Classes                
###########################################################
class RepositoryCreate(BaseModel):
    name: str

class Repository(BaseModel):
    id: UUID
    name: str
    description: Optional[str] = None
    
class PermissionsRepo(BaseModel):
    user_id: UUID
    repository_id: UUID
    permission_level: str

