import os
from typing import Optional
from datetime import datetime, date
from fastapi import APIRouter, HTTPException, status, Form, UploadFile, File, Query
from src.core.settings.config import settings
from src.app.legends.services import LegendService, CategoryService, ProvinceService
from src.app.legends.schemas import LegendCreate, LegendsListResponse, LegendResponse, LegendUpdate, CategoryListResponse, ProvinceListResponse


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
            "/", self.create_legend, methods=["POST"], response_model=LegendResponse, status_code=status.HTTP_201_CREATED)
        self.router.add_api_route(
            "/", self.get_legends, methods=["GET"], response_model=LegendsListResponse, status_code=status.HTTP_200_OK)
        self.router.add_api_route(
            "/{legend_id}", self.get_legend, methods=["GET"], response_model=LegendResponse, status_code=status.HTTP_200_OK)
        self.router.add_api_route(
            "/{legend_id}", self.update_legend, methods=["PATCH"], status_code=status.HTTP_200_OK)
        self.router.add_api_route(
            "/{legend_id}", self.delete_legend, methods=["DELETE"], status_code=status.HTTP_200_OK)

    def get_legends(self, title: str = Query(None, description="Text to search legends"), category: int = Query(None, description="Category ID")):
        """Endpoint to get all legends."""
        try:
            legends = self.service.get_legends(title, category)
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

    def get_legend(self, legend_id: int):
        """Endpoint to get a legend."""
        try:
            legend = self.service.get_legend(legend_id)
            return legend

        except HTTPException as http_ex:
            raise http_ex

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e),
            )

    async def create_legend(self, title: str = Form(...), description: str = Form(...), category_id: int = Form(..., alias="categoryId"), district_id: int = Form(..., alias="districtId"), date: date = Form(...), image: UploadFile = File(...)):
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

            schema = LegendCreate(
                title=title,
                description=description,
                category_id=category_id,
                district_id=district_id,
                date=date,
                image=image_url
            )

            data = schema.model_dump()
            print(data)
            legend = self.service.create_legend(data)
            return legend

        except HTTPException as http_ex:
            raise http_ex

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e),
            )

    async def update_legend(self, legend_id: int, title: str = Form(None), description: str = Form(None), category_id: int = Form(None, alias="categoryId"), district_id: int = Form(None, alias="districtId"), date: date = Form(None), image: UploadFile = File(None)):
        """Endpoint to update a legend."""
        try:
            image_url = None
            if image:
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

            schema = LegendUpdate(
                title=title,
                description=description,
                category_id=category_id,
                district_id=district_id,
                date=date,
                image=image_url
            )

            data = schema.model_dump(exclude_none=True)

            if not data:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="No fields provided for update",
                )

            self.service.update_legend(legend_id, data)

            return {"message": "Legend updated successfully"}

        except HTTPException as http_ex:
            raise http_ex

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e),
            )

    def delete_legend(self, legend_id: int):
        """Endpoint to delete a legend."""
        try:
            self.service.delete_legend(legend_id)
            return {"message": "Legend deleted successfully"}

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
        self.router.add_api_route(
            "/", self.get_categories, methods=["GET"], response_model=CategoryListResponse, status_code=status.HTTP_200_OK)

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


class ProvinceRoutes:
    def __init__(self, service: ProvinceService):
        self.service = service
        self.router = APIRouter(
            prefix="/provinces",
            tags=["Provinces"],
        )
        self._register_routes()

    def get_router(self):
        return self.router

    def _register_routes(self):
        self.router.add_api_route(
            "/", self.get_provinces, methods=["GET"], response_model=ProvinceListResponse, status_code=status.HTTP_200_OK)

    def get_provinces(self):
        """Endpoint to get all provinces."""
        try:
            provinces = self.service.get_provinces()

            if not provinces:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="No provinces found",
                )
            return provinces

        except HTTPException as http_ex:
            raise http_ex
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e),
            )
