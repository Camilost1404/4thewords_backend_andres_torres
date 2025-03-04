from sqlalchemy.orm import joinedload
from fastapi import HTTPException, status
from sqlalchemy import or_

from src.app.legends.models import Legend, District, Canton, Province, Category
from src.core.db.db import Database


class LegendRepository:
    def __init__(self, db: Database):
        self.db = db

    def get_all(self, title: str = None, category: int = None):
        with self.db.get_session() as session:
            try:
                query = session.query(Legend).options(
                    joinedload(Legend.category),
                    joinedload(Legend.district).joinedload(
                        District.canton).joinedload(Canton.province)
                )
                if title:
                    # Busca coincidencias en título y descripción (caso insensible)
                    query = query.filter(
                        or_(
                            Legend.title.ilike(f"%{title}%")
                        )
                    )

                if category:
                    query = query.filter(Legend.category_id == category)

                legends = query.all()

                return legends
            except Exception as e:
                raise e

    def insert(self, legend: Legend):
        with self.db.get_session() as session:
            try:
                category_exists = session.query(Category.id).filter(
                    Category.id == legend.category_id).first()
                if not category_exists:
                    raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Category with id {legend.category_id} does not exist."
                    )

                district_exists = session.query(District.id).filter(
                    District.id == legend.district_id).first()
                if not district_exists:
                    raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"District with id {legend.district_id} does not exist."
                    )

                legend.title = legend.title.strip().capitalize()

                session.add(legend)
                session.commit()
                session.refresh(legend)

                legend = session.query(Legend).options(
                    joinedload(Legend.category),
                    joinedload(Legend.district).joinedload(
                        District.canton).joinedload(Canton.province)
                ).filter(Legend.id == legend.id).first()

                return legend
            except Exception as e:
                session.rollback()
                raise e

    def update(self, legend_id: int, update_data: dict):
        with self.db.get_session() as session:
            legend = (
                session.query(Legend)
                .options(joinedload(Legend.category), joinedload(Legend.district).joinedload(District.canton).joinedload(Canton.province))
                .filter(Legend.id == legend_id)
                .first()
            )

            if not legend:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Legend with id {legend_id} not found",
                )

            for key, value in update_data.items():
                setattr(legend, key, value)

            session.commit()
            session.refresh(legend)
            return legend
    
    def delete(self, legend_id: int):
        with self.db.get_session() as session:
            legend = session.query(Legend).filter(Legend.id == legend_id).first()

            if not legend:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Legend with id {legend_id} not found",
                )

            session.delete(legend)
            session.commit()
            return legend


class CategoryRepository:
    def __init__(self, db: Database):
        self.db = db

    def get_all(self):
        with self.db.get_session() as session:
            try:
                categories = session.query(Category).order_by(
                    Category.name.asc()).all()
                return categories
            except Exception as e:
                raise e
