from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class EnvBaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8", 
        case_sensitive=False,
        strict=True
    )

    
class BotSettings(EnvBaseSettings):
    bot_token: SecretStr

    
class Settings(BotSettings):
    pass


config = Settings()