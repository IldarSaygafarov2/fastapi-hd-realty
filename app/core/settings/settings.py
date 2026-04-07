from functools import lru_cache

from pydantic_settings import BaseSettings

from .app import AppSettings, AppConnectionSettings
from .cors import CORSSettings


class Settings(BaseSettings):
    app_settings: AppSettings = AppSettings()
    app_connection: AppConnectionSettings = AppConnectionSettings()
    cors_settings: CORSSettings = CORSSettings()


@lru_cache()
def get_settings():
    return Settings()
