import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.core.settings.config import settings
from src.core.db.db import database
from src.app.legends.routes import LegendRoutes
from src.app.legends.services import LegendService
from src.app.legends.repository import LegendRepository
from fastapi.middleware.cors import CORSMiddleware

os.makedirs(f'{settings.UPLOAD_FOLDER}', exist_ok=True)

# Repositories
legend_repository = LegendRepository(database)

# Services
legend_service = LegendService(legend_repository)

# Routes
legend_router = LegendRoutes(legend_service)

app = FastAPI()
app.title = settings.app_name

@app.on_event("startup")
async def startup_event():
    database._check_connection()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/uploads", StaticFiles(directory=settings.UPLOAD_FOLDER), name="uploads")
app.include_router(legend_router.get_router(), prefix="/api")