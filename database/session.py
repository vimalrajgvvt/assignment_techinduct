from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./address_book.db" # Using SQLite for local persistence as requested

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db(): # Dependency to get DB session in controllers
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()