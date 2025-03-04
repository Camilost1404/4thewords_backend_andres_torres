from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date
from sqlalchemy.orm import relationship

from src.core.db.db import database

Base = database.get_base()


class Category(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    legends = relationship("Legend", back_populates="category")

    def __repr__(self):
        return f"<Category {self.name}>"

    def __str__(self):
        return self.name


class Province(Base):
    __tablename__ = "provincias"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    cantones = relationship("Canton", back_populates="province")

    def __repr__(self):
        return f"<Provincia {self.name}>"

    def __str__(self):
        return self.name


class Canton(Base):
    __tablename__ = "cantones"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    province_id = Column(ForeignKey("provincias.id"))
    province = relationship("Province", back_populates="cantones")
    districts = relationship("District", back_populates="canton")

    def __repr__(self):
        return f"<Canton {self.name}>"

    def __str__(self):
        return f"{self.province_id}, {self.name}"


class District(Base):
    __tablename__ = "distritos"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    canton_id = Column(ForeignKey("cantones.id"))
    canton = relationship("Canton", back_populates="districts")
    legends = relationship("Legend", back_populates="district")

    def __repr__(self):
        return f"<District {self.name}>"

    def __str__(self):
        return f"{self.name} ({self.canton_id})"


class Legend(Base):
    __tablename__ = "leyendas"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(String(255), nullable=False, index=True)
    category_id = Column(ForeignKey("categorias.id"))
    category = relationship("Category", back_populates="legends")
    date = Column(Date, nullable=False)
    district_id = Column(ForeignKey("distritos.id"))
    district = relationship("District", back_populates="legends")
    image = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f"<Legend {self.title}>"

    def __str__(self):
        return self.title
