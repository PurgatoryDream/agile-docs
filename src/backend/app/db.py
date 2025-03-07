from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .conf import DATABASE_URL

###########################################################
######### DB Configuration:               
###########################################################
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
