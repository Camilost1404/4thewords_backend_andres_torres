from pydantic import BaseModel
from datetime import date

# Esquema para la creación de una leyenda (entrada)
class LegendCreate(BaseModel):
    # TODO Add validations for the fields
    
    title: str
    description: str
    category_id: int
    district_id: int
    date: date