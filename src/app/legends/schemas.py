from typing import Optional
from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, AliasGenerator, field_validator, RootModel
from pydantic.alias_generators import to_camel, to_snake

# Esquema para la creación de una leyenda (entrada)
class ProvinceResponse(BaseModel):
    id: int
    name: str

class CantonResponse(BaseModel):
    id: int
    name: str
    province: ProvinceResponse

class DistrictResponse(BaseModel):
    id: int
    name: str
    canton: CantonResponse

class CategoryResponse(BaseModel):
    id: int
    name: str
class LegendCreate(BaseModel):
    # TODO Add validations for the fields
    
    title: str
    description: str
    category_id: int
    district_id: int
    date: date
    
    model_config = ConfigDict(
        title = "Legend Create",
        alias_generator = AliasGenerator(
            validation_alias=to_snake,
            serialization_alias=to_camel,
        ),
    )
    
    @field_validator("title")
    def validate_title(cls, value):
        if not value or not value.strip():
            raise ValueError("Title is required")
        
        return value
    
    @field_validator("description")
    def validate_description(cls, value):
        if not value or not value.strip():
            raise ValueError("Description is required")
        
        return value

class LegendResponse(BaseModel):
    id: int
    title: str
    description: str
    category: CategoryResponse
    district: DistrictResponse
    date: date
    created_at: datetime

    model_config = ConfigDict(
        title = "Legend Response",
        alias_generator = AliasGenerator(
            validation_alias=to_snake,
            serialization_alias=to_camel,
        ),
    )

class LegendsListResponse(RootModel):
    root: list[LegendResponse]

class LegendUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category_id: Optional[int] = None
    district_id: Optional[int] = None
    date: Optional[date] = None
    
    model_config = ConfigDict(
        title = "Legend Update",
        alias_generator = AliasGenerator(
            validation_alias=to_snake,
            serialization_alias=to_camel,
        ),
    )
    
    @field_validator("title", mode="before")
    def validate_title(cls, value):
        if value is not None and not value.strip():
            raise ValueError("Title cannot be empty")
        return value.capitalize() if value else None

    @field_validator("description", mode="before")
    def validate_description(cls, value):
        if value is not None and not value.strip():
            raise ValueError("Description cannot be empty")
        return value if value else None