"""Module for creating database connections"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from .config import Settings

settings = Settings()

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": True},
    echo=True,
)

SessionLocal = sessionmaker(engine)

Base = declarative_base()
