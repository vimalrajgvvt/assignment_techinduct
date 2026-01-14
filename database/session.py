from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import Base

# [cite_start]Using SQLite for local persistence as requested [cite: 8]
SQLALCHEMY_DATABASE_URL = "sqlite:///./address_book.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get DB session in controllers
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()