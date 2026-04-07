from pydantic_settings import BaseSettings
from pydantic import PostgresDsn


class DatabaseSettings(BaseSettings):
    POSTGRES_DSN: PostgresDsn = "postgres://user:pass@localhost:5432/foobar"
