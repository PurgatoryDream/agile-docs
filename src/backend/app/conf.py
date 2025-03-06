import os
import dotenv
import logging
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext

###########################################################
######### Configuration:               
########################################################### 
dotenv.load_dotenv()
logging.getLogger('passlib').setLevel(logging.ERROR)

SECRET_KEY = os.getenv("SECRET_KEY_OPENSSL")
ALGORITHM = "HS256"
ACCESSS_TOKEN_EXPIRE_MINUTES = 30
REPO_PATH = os.path.join(os.getcwd(), "dev_files", "repository")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
