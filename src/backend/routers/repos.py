###########################################################
# repos.py
#----------------------------------------------------------
### Handles creation of new repositories, managing their
### files, etc.      
###########################################################
######### Imports                  
###########################################################
from git import Repo
from uuid import UUID
from datetime import datetime, timedelta, timezone
from typing import Annotated, List, Optional
from fastapi import Depends, HTTPException, status, APIRouter

from .auth import get_current_active_user
from ..models.user import User, UserDB
from ..models.repos import Repository, PermissionsRepo
from ..dependencies import fake_db
from ..conf import REPO_PATH

###########################################################
######### Helper functions       
###########################################################
async def get_user_repo_perms(db, user_id):
	permissions = []
	for perm in db["permissions"]:
		perm_obj = PermissionsRepo(**perm)
		if perm_obj.user_id == user_id:
			permissions.append(perm_obj)
	return permissions

###########################################################
######### Routes (repos):
###########################################################
router = APIRouter(
    prefix="/repos",
    tags=["repos"]
)

@router.get("/")
async def get_repo_list(
    current_user: Annotated[User, Depends(get_current_active_user)]
) -> List[PermissionsRepo]:
	return get_user_repo_perms(fake_db, current_user.id)

@router.post("/create")
async def create_new_repo(
	current_user: Annotated[User, Depends(get_current_active_user)],
	repo_name: str
) -> Repository:
	...
