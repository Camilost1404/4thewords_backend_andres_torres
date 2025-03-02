from fastapi import FastAPI

from src.core.settings.config import settings
from src.core.db.db import database
from src.app.legends.dependencies import get_legend_routes

app = FastAPI(root_path="/api")
app.title = settings.app_name

# Routes
legend_router = get_legend_routes()


@app.on_event("startup")
async def startup_event():
    database._check_connection()

app.include_router(legend_router.get_router())

@app.get("/")
def read_root():
    return {"Hello": "World"}