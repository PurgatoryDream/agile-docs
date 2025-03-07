import os
import dotenv
import uvicorn
import logging
import json
from fastapi import FastAPI

from .conf import *
from .routers import auth, repos

###########################################################
######### Configuration
###########################################################
app = FastAPI()
app.include_router(auth.router)
app.include_router(repos.router)

###########################################################
######### Routes:
###########################################################
@app.get("/")
def hello_world():
    return {"status": "ok!"}
