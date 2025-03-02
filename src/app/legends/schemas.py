from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, AliasGenerator, field_validator, RootModel
from pydantic.alias_generators import to_camel, to_snake

# Esquema para la creación de una leyenda (entrada)
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
    category_id: int
    district_id: int
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