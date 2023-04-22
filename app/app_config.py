from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    db_name: str = "fastapi_masonite"
    db_driver: str = "postgres"
    db_host: str = "localhost"
    db_port: int = 5432
    db_user: str
    db_password: str
    db_log_queries = True


@lru_cache()
def get_settings():
    return Settings(_env_file='.env')
