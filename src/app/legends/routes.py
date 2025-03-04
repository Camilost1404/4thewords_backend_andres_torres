import os
from datetime import datetime, date
from fastapi import APIRouter, HTTPException, status, Form, UploadFile, File, Query
from src.core.settings.config import settings
from src.app.legends.services import LegendService, CategoryService
from src.app.legends.schemas import LegendCreate, LegendsListResponse, LegendResponse, LegendUpdate, CategoryListResponse


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
        self.router.add_api_route(
            "/", self.create_legend, methods=["POST"], response_model=LegendResponse)
        self.router.add_api_route(
            "/", self.get_legends, methods=["GET"], response_model=LegendsListResponse)
        self.router.add_api_route(
            "/{legend_id}", self.update_legend, methods=["PATCH"], response_model=LegendResponse)

    def get_legends(self, title: str = Query(None, description="Texto para buscar leyendas")):
        """Endpoint to get all legends."""
        try:
            legends = self.service.get_legends(title)
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

    async def create_legend(self, title: str = Form(...), description: str = Form(...), category_id: int = Form(...), district_id: int = Form(...), date: date = Form(...), image: UploadFile = File(...)):
        """Endpoint to create a new legend."""
        try:
            if not image.content_type.startswith("image/"):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid file type. Only images are allowed",
                )

            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            file_name = f"{timestamp}_{image.filename}"
            file_path = os.path.join(settings.UPLOAD_FOLDER, file_name)

            with open(file_path, "wb") as buffer:
                buffer.write(await image.read())

            image_url = f"{settings.IMAGE_URL}/uploads/{file_name}"

            schema = LegendCreate(title=title, description=description, category_id=category_id,
                                  district_id=district_id, date=date, image=image_url)

            data = schema.model_dump()
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

class CategoryRoutes:
    def __init__(self, service: CategoryService):
        self.service = service
        self.router = APIRouter(
            prefix="/categories",
            tags=["Categories"],
        )
        self._register_routes()

    def get_router(self):
        return self.router

    def _register_routes(self):
        self.router.add_api_route("/", self.get_categories, methods=["GET"], response_model=CategoryListResponse)

    def get_categories(self):
        """Endpoint to get all categories."""
        try:
            categories = self.service.get_categories()

            if not categories:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="No categories found",
                )
            return categories

        except HTTPException as http_ex:
            raise http_ex
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e),
            )
