from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.core.settings.config import settings
class Database:
    def __init__(self, db_url: str):
        print(f"Database URL: {db_url}")
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        self.Base = declarative_base()
    
    def _check_connection(self):
        try:
            with self.engine.connect() as connection:
                print("Connection successful")
        except Exception as e:
            print(f"Connection error: {e}")
        finally:
            self.engine.dispose

    def get_base(self):
        return self.Base
    
    def get_session(self):
        return self.Session()

database = Database(settings.database_url)

def get_db():
    db = database.get_session()
    try:
        yield db
    finally:
        db.close()