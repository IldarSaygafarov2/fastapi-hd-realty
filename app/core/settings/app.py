from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    APP_NAME: str = "HD Realty API"
    API_VERSION: str = "1.0.0"


class AppConnectionSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000
