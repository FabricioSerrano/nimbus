from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):

    data_url : str
    log_level : str
    log_dir : str
    mqhost : str
    mqqueue : str

    model_config = SettingsConfigDict(
        env_file='.env', 
        env_file_encoding='utf-8'
    )
