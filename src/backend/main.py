import os

import uvicorn
from fastapi import FastAPI

# Initialiaze the app:
app = FastAPI()

@app.get("/test")
def hello_world():
    return {"response": "Hello World!"}
