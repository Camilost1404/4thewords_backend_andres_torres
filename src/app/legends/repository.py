from sqlalchemy.orm import Session

class LegendRepository:
    def __init__(self, db: Session):
        self.db = db
    
    async def insert(self, legend):
        try:
            self.db.add(legend)
            self.db.commit()
            self.db.refresh(legend)
            return legend
        except Exception as e:
            self.db.rollback()
            raise e