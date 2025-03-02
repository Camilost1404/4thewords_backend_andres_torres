from fastapi import APIRouter, HTTPException, status

from src.app.legends.services import LegendService
from src.app.legends.schemas import LegendCreate, LegendsListResponse

class LegendRoutes:
    def __init__(self, service: LegendService):
        self.service = service
        self.router = APIRouter(
            prefix="/legends",
            tags=["Legends"],
        )
        self._register_routes()

    def get_router(self):
        """Returns the router."""
        return self.router
    
    def _register_routes(self):
        """Register routes."""
        self.router.add_api_route("/", self.create_legend, methods=["POST"])
        self.router.add_api_route("/", self.get_legends, methods=["GET"])
        
    def get_legends(self):
        """Endpoint to get all legends."""
        try:
            legends = self.service.get_legends()
            return LegendsListResponse.parse_obj(legends)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e),
            )
    
    async def create_legend(self, request: LegendCreate):
        """Endpoint to create a new legend."""
        try:
            data = request.model_dump()
            legend = await self.service.create_legend(data)
            return legend
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e),
            )
