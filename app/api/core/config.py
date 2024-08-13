from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    PROJECT_NAME: str = "Cadastral Service"
    POSTGRES_DB: str = Field(default='cadastral_db', env='POSTGRES_DB')
    POSTGRES_USER: str = Field(default='postgres', env='POSTGRES_USER')
    POSTGRES_PASSWORD: str = Field(default='12345', env='POSTGRES_PASSWORD')
    POSTGRES_HOST: str = Field(default='127.0.0.1', env='POSTGRES_HOST')
    POSTGRES_PORT: int = Field(default=5432, env='POSTGRES_PORT')
    SECRET_KEY: str = Field(default='supersecretkey', env='SECRET_KEY')
    ALGORITHM: str = Field(default='HS256', env='ALGORITHM')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30, env='ACCESS_TOKEN_EXPIRE_MINUTES')

    TEST_POSTGRES_DB: str = Field(default='test_cadastral_db', env='TEST_POSTGRES_DB')


settings = Settings()
