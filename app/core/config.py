from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "FitLife"
    app_version: str = "0.1.0"
    debug: bool = False

    jwt_secret_key: str
    jwt_algorithm: str ="HS256"
    access_token_expire_minutes: int = 30

    database_url: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"

    )

setiings = Settings()