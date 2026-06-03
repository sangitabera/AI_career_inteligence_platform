from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str

    API_HOST: str
    API_PORT: int

    redis_host: str = 'localhost'
    redis_port: int = 6379

    RATE_LIMIT: str
    LOG_LEVEL: str

    model_config = SettingsConfigDict(
        env_file = ".env"
    )

settings = Settings()