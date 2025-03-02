from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from src.core.db.db import get_db
from src.app.legends.repository import LegendRepository
from src.app.legends.services import LegendService
from src.app.legends.routes import LegendRoutes

def get_legend_repository(db: Annotated[Session, Depends(get_db)]) -> LegendRepository:
    return LegendRepository(db=db)

def get_legend_service(legend_repository: Annotated[LegendRepository, Depends(get_legend_repository)]) -> LegendService:
    return LegendService(repository=legend_repository)

def get_legend_routes(legend_service: Annotated[LegendService, Depends(get_legend_service)]) -> LegendRoutes:
    return LegendRoutes(legend_service=legend_service)