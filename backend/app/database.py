from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

database_url = "sqlite:///./data/app.db"

engine = create_engine(
    database_url,
    connect_args={"check_same_thread": False},
)

session_local = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)

class Base(DeclarativeBase):
    pass

def get_db() -> Generator:
    db = session_local()
    try:
        yield db
    finally:
        db.close()