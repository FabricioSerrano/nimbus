import logging
from schemas.city_schema import CitySchema
from models.city import City
from models.base import Base
from controllers import engine
from sqlalchemy.orm import Session


logger = logging.getLogger('controllers.data_controller')

class DataController:
    def __init__(self):
        Base.metadata.create_all(engine)

    
    def push_data(self, city : CitySchema) -> None:

        orm_city = City(
            codigo_ibge=city.codigo_ibge,
            nome_municipio=city.nome_municipio,
            capital=city.capital,
            codigo_uf=city.codigo_uf,
            uf=city.uf,
            estado=city.estado,
            latitude=city.latitude,
            longitude=city.longitude
        )

        session = Session(engine)

        if session.query(City).filter(City.codigo_ibge == orm_city.codigo_ibge).first() is not None:
            session.close()
            return

        session.add(orm_city)

        session.commit()

        session.close()
        
    
