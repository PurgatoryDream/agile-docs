###########################################################
######### Imports                  
########################################################### 
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID

from .user import User

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
