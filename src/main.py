from fastapi import FastAPI
from src.core.settings.config import settings

app = FastAPI()
app.title = settings.app_name

@app.get("/")
def read_root():
    return {"Hello": "World"}