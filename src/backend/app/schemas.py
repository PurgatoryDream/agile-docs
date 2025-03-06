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
class User(BaseModel):
    id: UUID
    username: str
    email: str | None = None
    
class UserDB(User):
    hashed_password: str

###########################################################
######### Repository Classes                
########################################################### 
class Repository(BaseModel):
    id: UUID
    name: str
    description: Optional[str] = None
    owner_id: UUID
    
class PermissionsRepo(BaseModel):
    user_id: UUID
    repository_id: UUID
    permission_level: str

