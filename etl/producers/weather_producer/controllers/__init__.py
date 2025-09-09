from sqlalchemy import create_engine
from utils.settings import Settings


settings = Settings()

database_url = f"mysql+mysqlconnector://{settings.mysqluser}:{settings.mysqlpass}@{settings.mysqlhost}:3306/{settings.mysqldatabase}"

engine = create_engine(database_url, future=True)