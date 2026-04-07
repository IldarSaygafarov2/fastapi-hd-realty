from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    POSTGRES_DSN: PostgresDsn = "postgres://user:pass@localhost:5432/foobar"
