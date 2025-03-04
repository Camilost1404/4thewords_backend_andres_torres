import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.core.settings.config import settings
from src.core.db.db import database
from src.app.legends.routes import LegendRoutes, CategoryRoutes, ProvinceRoutes
from src.app.legends.services import LegendService, CategoryService, ProvinceService
from src.app.legends.repository import LegendRepository, CategoryRepository, ProvinceRepository
from fastapi.middleware.cors import CORSMiddleware

os.makedirs(f'{settings.UPLOAD_FOLDER}', exist_ok=True)

# Repositories
legend_repository = LegendRepository(database)
category_repository = CategoryRepository(database)
province_repository = ProvinceRepository(database)

# Services
legend_service = LegendService(legend_repository)
category_service = CategoryService(category_repository)
province_service = ProvinceService(province_repository)

# Routes
legend_router = LegendRoutes(legend_service)
category_router = CategoryRoutes(category_service)
province_router = ProvinceRoutes(province_service)

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
app.include_router(category_router.get_router(), prefix="/api")
app.include_router(province_router.get_router(), prefix="/api")