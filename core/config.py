"""Application configuration"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings
    """
    DATABASE_URL: str

    class Config:
        """Environment configuration"""
        env_file = ".env"
