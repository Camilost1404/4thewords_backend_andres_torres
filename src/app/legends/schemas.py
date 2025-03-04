from typing import Optional
from datetime import date as dt, datetime

from fastapi import HTTPException
from pydantic import BaseModel, ConfigDict, AliasGenerator, field_validator, RootModel
from pydantic.alias_generators import to_camel, to_snake

# Esquema para la creación de una leyenda (entrada)


class CategoryInfo(BaseModel):
    id: int
    name: str


class ProvinceInfo(BaseModel):
    id: int
    name: str


class CantonInfo(BaseModel):
    id: int
    name: str
    province: ProvinceInfo


class DistrictInfo(BaseModel):
    id: int
    name: str
    canton: CantonInfo


class LegendResponse(BaseModel):
    id: int
    title: str
    description: str
    category: CategoryInfo
    district: DistrictInfo
    date: dt
    image: str
    created_at: datetime

    model_config = ConfigDict(
        title="Legend Response",
        alias_generator=AliasGenerator(
            validation_alias=to_snake,
            serialization_alias=to_camel,
        ),
    )

class CategoryResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(
        title="Category Response",
        alias_generator=AliasGenerator(
            validation_alias=to_snake,
            serialization_alias=to_camel,
        ),
    )

class DistrictsInfo(BaseModel):
    id: int
    name: str

class CantonsInfo(BaseModel):
    id: int
    name: str
    districts: list[DistrictsInfo]

class ProvinceResponse(BaseModel):
    id: int
    name: str
    cantones: list[CantonsInfo]
    
    model_config = ConfigDict(
        title="Province Response",
        alias_generator=AliasGenerator(
            validation_alias=to_snake,
            serialization_alias=to_camel,
        ),
    )


class LegendCreate(BaseModel):
    # TODO Add validations for the fields

    title: str
    description: str
    category_id: int
    district_id: int
    date: dt
    image: str

    model_config = ConfigDict(
        title="Legend Create",
        alias_generator=AliasGenerator(
            validation_alias=to_snake,
            serialization_alias=to_camel,
        ),
    )

    @field_validator("title")
    def validate_title(cls, value):
        if not value or not value.strip():
            raise HTTPException(status_code=400, detail="Title is required")

        return value

    @field_validator("description")
    def validate_description(cls, value):
        if not value or not value.strip():
            raise HTTPException(
                status_code=400, detail="Description is required")

        return value


class LegendsListResponse(RootModel):
    root: list[LegendResponse]


class CategoryListResponse(RootModel):
    root: list[CategoryInfo]

class ProvinceListResponse(RootModel):
    root: list[ProvinceResponse]


class LegendUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category_id: Optional[int] = None
    district_id: Optional[int] = None
    date: dt | None = None
    image: Optional[str] = None

    model_config = ConfigDict(
        title="Legend Update",
        alias_generator=AliasGenerator(
            validation_alias=to_snake,
            serialization_alias=to_camel,
        ),
    )

    @field_validator("title", mode="before")
    def validate_title(cls, value):
        if value is not None and not value.strip():
            raise HTTPException(
                status_code=400, detail="Title cannot be empty")
        return value.capitalize() if value else None

    @field_validator("description", mode="before")
    def validate_description(cls, value):
        if value is not None and not value.strip():
            raise HTTPException(
                status_code=400, detail="Description cannot be empty")
        return value if value else None
