from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):

    loglevel : str
    mqhost : str
    mqqueue : str
    mquser : str
    mqpass : str
    mysqlhost : str
    mysqluser : str
    mysqlpass : str
    mysqldatabase: str
    openmeteourl : str

    model_config = SettingsConfigDict(
        env_file='.env', 
        env_file_encoding='utf-8'
    )
