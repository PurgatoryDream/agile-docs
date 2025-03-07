import os
import dotenv
import logging
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext

###########################################################
######### Configuration:               
########################################################### 
dotenv.load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))
logging.getLogger('passlib').setLevel(logging.ERROR)

SECRET_KEY = os.getenv("SECRET_KEY_OPENSSL")
ALGORITHM = "HS256"
ACCESSS_TOKEN_EXPIRE_MINUTES = 30
REPO_PATH = os.path.join(os.getcwd(), "dev_files", "repository")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
