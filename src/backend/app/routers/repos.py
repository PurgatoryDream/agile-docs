###########################################################
# repos.py
#----------------------------------------------------------
### Handles creation of new repositories, managing their
### files, etc.      
###########################################################
import os
import sys
import git
import uuid
from uuid import UUID
from datetime import datetime, timedelta, timezone
from typing import Annotated, List, Optional
from fastapi import Depends, HTTPException, status, APIRouter

from .auth import get_current_active_user
from ..schemas import User, UserDB, Repository, PermissionsRepo
from ..dependencies import fake_db
from ..conf import REPO_PATH

###########################################################
######### Helper functions       
###########################################################
def get_user_repo_perms(db, user_id):
	permissions = []
	for perm in db["permissions"]:
		perm_obj = PermissionsRepo(**perm)
		if perm_obj.user_id == user_id:
			permissions.append(perm_obj)
	return permissions

def create_new_repo(db, user_id, repo_name):
	if repo_name in db["repositories"]:
		return False
	
	# Create the folder and initialize a repo:
	repo_folder = os.path.join(REPO_PATH, repo_name)
	os.mkdir(repo_folder)
	repo = git.Repo.init(repo_folder)

	# Insert in database:
	repo_uuid = uuid.uuid4()
	repo_uuid_str = str(repo_uuid)
	db["repositories"][repo_uuid_str] = {
		"id": repo_uuid_str,
		"name": repo_name,
		"description": "",
		"owner_id": repo_uuid_str
	}

	return Repository(**db["repositories"][repo_uuid_str])

def get_existing_repo(db, user_id, repo_name: str):
	if repo_name not in db["repositories"]:
		return False
	
	# Check if the user has permissions for this repo:
	repo_data = Repository(**db["repositories"][repo_name])
	user_permissions = get_user_repo_perms(db, user_id)
	allowed = False
	for perm in user_permissions:
		if perm.user_id == user_id and perm.repository_id == repo_data.id:
			allowed = True
	if not allowed:
		return False

	# Get the repository object:
	repo_folder = os.path.join(REPO_PATH, repo_name)
	repo = git.Repo(repo_folder)
	return repo

def add_files_repo(repo: git.Repo, files: List[str]):
	repo.index.add(files)
	return True

def commit_changes(repo: git.Repo, commit_message: str = "[No message]."):
	commit = repo.index.commit(commit_message)
	return commit.hexsha

def rollback_to_commit(repo: git.Repo, commit_hash: str):
	git_cmd = repo.git
	try:
		git_cmd.reset("--hard", commit_hash)
		return True
	except Exception as e:
		print(f"Rollback failed: {e}")
		return False

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
async def new_repo(
	current_user: Annotated[User, Depends(get_current_active_user)],
	repo_name: str
) -> Repository:
	repo = create_new_repo(fake_db, current_user.id, repo_name)
	if not repo:
		raise HTTPException(
			status_code=status.HTTP_409_CONFLICT,
			detail="Repository with that name already exists."
		)
	return repo

@router.post("/add_files")
async def add_files(
	current_user: Annotated[User, Depends(get_current_active_user)],
	repo_name: str,
	files: List[str] | str = "*"
):
	repo = get_existing_repo(fake_db, current_user.id, repo_name)
	if not repo:
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="Repository does not exist for user."
		)
	
	if type(files) == str:
		files = [files]
	added = add_files_repo(repo, files)
	if not added:
		raise HTTPException(
			status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
			detail="Something went wrong."
		)
	
	return {"response": "Added files!"}

@router.post("/commit")
async def commit_repo(
	current_user: Annotated[User, Depends(get_current_active_user)],
	repo_name: str,
	message: str | None = None
):
	repo = get_existing_repo(fake_db, current_user.id, repo_name)
	if not repo:
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="Repository does not exist for user."
		)
	
	commited = commit_changes(repo, message)
	if not commited:
		raise HTTPException(
			status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
			detail="Something went wrong."
		)
	return {"response": "Commited!"}

@router.post("/rollback_commit")
async def rollback_commit(
	current_user: Annotated[User, Depends(get_current_active_user)],
	repo_name: str,
	commit_hash: str
):
	repo = get_existing_repo(fake_db, current_user.id, repo_name)
	if not repo:
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="Repository does not exist for user."
		)
	
	rollback = rollback_to_commit(repo, commit_hash)
	if not rollback:
		raise HTTPException(
			status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
			detail="Something went wrong."
		)
	return {"response": f"Rolled back to {commit_hash}!"}
