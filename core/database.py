"""Module for creating database connections"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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
