###########################################################
######### Imports                  
########################################################### 
from pydantic import BaseModel

###########################################################
######### Auth Classes                
########################################################### 
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: str | None = None
