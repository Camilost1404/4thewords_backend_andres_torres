from fastapi import FastAPI
from src.core.settings.config import settings
from src.core.db.db import database

app = FastAPI()
app.title = settings.app_name

@app.on_event("startup")
async def startup_event():
    database._check_connection()

@app.get("/")
def read_root():
    return {"Hello": "World"}