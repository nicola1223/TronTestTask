"""Module for dependencies"""
from core.database import SessionLocal


async def get_db():
    """Provide a database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
