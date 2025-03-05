###########################################################
######### Imports                  
########################################################### 
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID

###########################################################
######### Auth Classes                
########################################################### 
class User(BaseModel):
    id: UUID
    username: str
    email: str | None = None
    
class UserDB(User):
    hashed_password: str
