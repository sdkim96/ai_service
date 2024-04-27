from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Name of this App
    app_name: str

    openai_key: str
    mysql_host: str
    mysql_user: str
    mysql_db: str
    mysql_password: str
    mysql_port: int


    _callback: any = None
    _sessionlog: any = None

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')
    print(f"model_config : {model_config}")
    
@lru_cache
def get_settings():
    return Settings()
