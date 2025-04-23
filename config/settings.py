from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    """
    Loads application settings from environment variables or a `.env` file.
    """

    debug:bool = False
    database_url:str = ''
    database_host:str = ''
    database_port:str = ''
    database_user:str = ''
    database_password:str = ''
    database_name:str = ''
    database_sslmode:str = ''

    class Config:
        env_file = ".env"

@lru_cache
def get_settings():
    """
    Loads and returns the application settings, cached for efficiency.
    """

    return Settings()

settings = get_settings()