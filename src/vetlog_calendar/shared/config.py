from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_host: str
    db_name: str
    db_user: str
    db_password: str
    TOKEN_PATH: str
    CREDENTIALS_PATH: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


@lru_cache
def get_settings():
    """
    Returns a cached instance of the Settings class.
    """
    """
    Returns a cached instance of Settings using lru_cache.
    This ensures that environment variables are read only once and
    repeated calls return the same Settings object.
    """
    return Settings()
