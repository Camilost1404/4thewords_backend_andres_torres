from fastapi import FastAPI

from src.core.settings.config import settings
from src.core.db.db import database
from src.app.legends.routes import LegendRoutes
from src.app.legends.services import LegendService
from src.app.legends.repository import LegendRepository

# Repositories
legend_repository = LegendRepository(database)

# Services
legend_service = LegendService(legend_repository)

# Routes
legend_router = LegendRoutes(legend_service)

app = FastAPI(root_path="/api")
app.title = settings.app_name

@app.on_event("startup")
async def startup_event():
    database._check_connection()

app.include_router(legend_router.get_router())