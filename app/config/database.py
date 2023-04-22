from masoniteorm.connections import ConnectionResolver
from app.app_config import get_settings

settings = get_settings()

DATABASES = dict(
  default="postgres",
  postgres=dict(
    host=settings.db_host,
    driver=settings.db_driver,
    database=settings.db_name,
    user=settings.db_user,
    password=settings.db_password,
    port=settings.db_port,
    log_queries=settings.db_log_queries,
    options=dict()
  )
)

DB = ConnectionResolver().set_connection_details(DATABASES)
