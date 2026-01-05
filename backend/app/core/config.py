from pydantic_settings import BaseSettings
from typing import Optional, List


class Settings(BaseSettings):
    # Database settings
    DATABASE_URL: str
    # JWT settings
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Application settings
    PROJECT_NAME: str = "Todo Evolution API"
    VERSION: str = "1.0.0"

    # CORS settings
    ALLOWED_ORIGINS: str = "*"  # Comma-separated string from env

    # Server settings
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    DEBUG: bool = True

    class Config:
        env_file = ".env"

    @property
    def parsed_allowed_origins(self) -> List[str]:
        """Parse ALLOWED_ORIGINS from comma-separated string to list."""
        if isinstance(self.ALLOWED_ORIGINS, str):
            return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",") if origin.strip()]
        return self.ALLOWED_ORIGINS


settings = Settings()