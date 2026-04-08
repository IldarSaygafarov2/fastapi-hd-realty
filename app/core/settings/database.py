from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    POSTGRES_DSN: PostgresDsn = "postgresql://user:pass@localhost:5432/foobar"
    ALEMBIC_DSN: str = "postgres://user:pass@localhost:5432/foobar"
