from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.core.settings.config import settings
class Database:
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        self.Base = declarative_base()

    def create_all(self):
        self.Base.metadata.create_all(self.engine)

    def drop_all(self):
        self.Base.metadata.drop_all(self.engine)

    def get_session(self):
        return self.Session()

database = Database(settings.database_url)

def get_db():
    db = database.get_session()
    try:
        yield db
    finally:
        db.close()