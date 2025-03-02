from sqlalchemy.orm import Session

from src.app.legends.models import Legend
from src.core.db.db import Database

class LegendRepository:
    def __init__(self, db: Database):
        self.db = db

    def insert(self, legend: Legend):
        with self.db.get_session() as session:
            try:
                session.add(legend)
                session.commit()
                session.refresh(legend)
                return legend
            except Exception as e:
                session.rollback()
                raise e
            finally:
                session.close()