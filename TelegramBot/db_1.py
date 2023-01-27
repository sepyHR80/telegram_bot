from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from .config import DB_URI

def start() -> scoped_session:
    engine = create_engine(DB_URL)