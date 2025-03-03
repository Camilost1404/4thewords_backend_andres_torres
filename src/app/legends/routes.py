from fastapi import APIRouter, HTTPException, status

from src.app.legends.services import LegendService
from src.app.legends.schemas import LegendCreate, LegendsListResponse, LegendResponse, LegendUpdate

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
        self.router.add_api_route("/", self.create_legend, methods=["POST"], response_model=LegendResponse)
        self.router.add_api_route("/", self.get_legends, methods=["GET"], response_model=LegendsListResponse)
        self.router.add_api_route("/{legend_id}", self.update_legend, methods=["PATCH"], response_model=LegendResponse)
        
    def get_legends(self):
        """Endpoint to get all legends."""
        try:
            legends = self.service.get_legends()
            
            if not legends:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="No legends found",
                )
            return legends
        
        except HTTPException as http_ex:
            raise http_ex

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e),
            )
        
    def create_legend(self, request: LegendCreate):
        """Endpoint to create a new legend."""
        try:
            data = request.model_dump()
            legend = self.service.create_legend(data)
            return legend

        except HTTPException as http_ex:
            raise http_ex
        
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e),
            )
    
    def update_legend(self, legend_id: int, request: LegendUpdate):
        """Endpoint to update a legend."""
        try:
            data = request.model_dump(exclude_unset=True)

            if not data:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="No fields provided for update",
                )

            updated_legend = self.service.update_legend(legend_id, data)

            return updated_legend
        
        except HTTPException as http_ex:
            raise http_ex

        except Exception as e:
            raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
            )
