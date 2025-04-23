from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
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
    return Settings()

settings = get_settings()