from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    env: str = "local"
    app_name: str = "Awesome API"
    database_url: str
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra = "ignore",
    )
    
settings = Settings()