from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TOKEN_PATH: str
    CREDENTIALS_PATH: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
