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
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter

from .auth import get_current_active_user
from ..db import get_db
from ..crud import get_user, get_repository, get_user_repositories, create_new_repo
from ..schemas import User, UserDB, Repository, RepositoryCreate, PermissionsRepo
from ..conf import REPO_PATH

###########################################################
######### Helper functions       
###########################################################
def create_new_repo_git(db, username, repo_name):
	# Check if the user already has a repo with that name:
	user_repos = get_user_repositories(db, username)
	for repo in user_repos:
		repo_id = repo.repository_id
		repo_data = get_repository(db, repo_id)
		if repo_data.name == repo_name:
			return False

	# Create the folder and initialize a repo:
	try:
		repo_folder = os.path.join(REPO_PATH, repo_name)
		os.mkdir(repo_folder)
		repo = git.Repo.init(repo_folder)
	except Exception as e:
		print(f"Error creating repo. {e}")
		return False

	# Insert in database:
	repo_data = RepositoryCreate(name=repo_name)
	db_repo, db_userperms = create_new_repo(db, username, repo_data)

	return Repository(**db_repo)

def get_existing_repo(db, username, repo_name: str):
	# Check if the user already has a repo with that name:
	found = False
	repo_data = None
	user_repos = get_user_repositories(db, username)
	for repo in user_repos:
		repo_id = repo.repository_id
		repo_data = get_repository(db, repo_id)
		if repo_data.name == repo_name:
			found = True
			break
	
	if not found:
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
    current_user: Annotated[User, Depends(get_current_active_user)],
	db: Annotated[Session, Depends(get_db)]
) -> List[PermissionsRepo]:
	return get_user_repositories(db, current_user.username)

@router.post("/create")
async def new_repo(
	current_user: Annotated[User, Depends(get_current_active_user)],
	repo_name: str,
	db: Annotated[Session, Depends(get_db)]
) -> Repository:
	repo = create_new_repo_git(db, current_user.username, repo_name)
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
	db: Annotated[Session, Depends(get_db)],
	files: List[str] | str = "*"
):
	repo = get_existing_repo(db, current_user.username, repo_name)
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
	db: Annotated[Session, Depends(get_db)],
	message: str | None = None
):
	repo = get_existing_repo(db, current_user.username, repo_name)
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
	commit_hash: str,
	db: Annotated[Session, Depends(get_db)]
):
	repo = get_existing_repo(db, current_user.username, repo_name)
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
