import os
import dotenv
import uvicorn
import logging
import json
from fastapi import FastAPI

from .conf import *
from .dependencies import fake_db
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

@app.get("/load_fake_db_from_json")
def get_fake_db_from_json():
    try:
        with open("fake_db.json", "r") as f:
            fake_db = json.loads(fake_db)
        return {"response": "ok!"}
    except Exception as e:
        print(f"Error while saving fake_db: {e}")
        return {"response": "bad"}

@app.get("/save_fake_db_to_json")
def save_fake_db_to_json():
    try:
        with open("fake_db.json", "w") as f:
            f.write(json.dumps(fake_db))
        return {"response": "ok!"}
    except Exception as e:
        print(f"Error while saving fake_db: {e}")
        return {"response": "bad"}
