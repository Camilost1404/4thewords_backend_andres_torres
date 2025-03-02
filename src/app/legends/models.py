from src.core.db.db import database
from sqlalchemy import Column, Integer, String

Base = database.get_base()

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    
    def __repr__(self):
        return f"<Category {self.name}>"
    
    def __str__(self):
        return self.name