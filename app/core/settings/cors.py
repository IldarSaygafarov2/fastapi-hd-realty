from pydantic_settings import BaseSettings


class CORSSettings(BaseSettings):
    ALLOWED_ORIGINS: list[str] = ["http://0.0.0.0"]
