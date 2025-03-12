###########################################################
# auth.py
#----------------------------------------------------------
### Handles all the authorization code, along with
### getting information from the user from the
### database.
###########################################################
from datetime import datetime, timedelta, timezone
from typing import Annotated
from sqlalchemy.orm import Session
from uuid import UUID

import jwt
from jwt.exceptions import InvalidTokenError
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from ..schemas import Token, TokenData, User, UserDB
from ..db import get_db
from ..crud import get_user, get_repository, get_user_repositories
from ..conf import SECRET_KEY, ALGORITHM, ACCESSS_TOKEN_EXPIRE_MINUTES, pwd_context, oauth2_scheme

###########################################################
######### Helper functions       
###########################################################
def verify_password(plain_password, hashed_password):
	return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
	return pwd_context.hash(password)

def authenticate_user(db, username: str, password: str):
	user = get_user(db, username)
	if not user:
		return False
	if not verify_password(password, user.hashed_password):
		return False
	return user

def create_access_token(
		data: dict, 
		expires_delta: timedelta | None = None
):
	to_encode = data.copy()
	if expires_delta:
		expire = datetime.now(timezone.utc) + expires_delta
	else:
		expire = datetime.now(timezone.utc) + timedelta(minutes=15)
	to_encode.update({"exp": expire})
	encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
	return encoded_jwt

async def get_current_user(
		token: Annotated[str, Depends(oauth2_scheme)],
		db: Annotated[Session, Depends(get_db)]
):
	credentials_exception = HTTPException(
		status_code=status.HTTP_401_UNAUTHORIZED,
		detail="Could not validate credentials.",
		headers={"WWW-Authenticate": "Bearer"}
	)
	try:
		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
		username = payload.get("sub")
		if username is None:
			raise credentials_exception
		token_data = TokenData(username=username)
	except InvalidTokenError:
		raise credentials_exception
	
	if token_data.username is None:
		raise credentials_exception

	user = get_user(db, username=token_data.username)
	if user is None:
		raise credentials_exception
	
	return user

async def get_current_active_user(
		current_user: Annotated[User, Depends(get_current_user)]
):
	return current_user

###########################################################
######### Routes (token, login/register):    
###########################################################
router = APIRouter()

@router.post("/auth/token", tags=["auth"])
async def login_for_access_token(
	form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
	db: Annotated[Session, Depends(get_db)]
) -> Token:
	credentials_exception = HTTPException(
		status_code=status.HTTP_401_UNAUTHORIZED,
		detail="Incorrect username or password.",
		headers={"WWW-Authenticate": "Bearer"}
	)
	user = authenticate_user(db, form_data.username, form_data.password)
	if not user:
		raise credentials_exception
	
	access_token_expires = timedelta(minutes=ACCESSS_TOKEN_EXPIRE_MINUTES)
	access_token = create_access_token(
		data={"sub": user.username}, expires_delta=access_token_expires
	)
	return Token(access_token=access_token, token_type="bearer")

###########################################################
######### Routes (user information):    
###########################################################
@router.post("/users/me/", response_model=User, tags=["user"])
async def read_users_me(
	current_user: Annotated[User, Depends(get_current_active_user)]
) -> User:
	return current_user
