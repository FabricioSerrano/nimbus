import logging
from schemas.weather_schema import WeatherSchema
from models.city import City
from models.weather import Weather
from models.base import Base
from controllers import engine
from sqlalchemy.orm import Session
from datetime import datetime


()

logger = logging.getLogger('controllers.data_controller')

class DataController:
    def __init__(self):
        Base.metadata.create_all(engine)

    
    def push_data(self, weather : WeatherSchema) -> None:

        orm_weather = Weather(
            data=datetime.fromtimestamp(weather.data),
            codigo_ibge=weather.codigo_ibge,
            codigo_uf=weather.codigo_uf,
            nome_municipio=weather.nome_municipio,
            uf=weather.uf,
            latitude=weather.latitude,
            longitude=weather.longitude,
            temperatura=weather.temperature_2m,
            humidade_relativa=weather.relative_humidity_2m,
            precipitacao=weather.precipitation,
            cobertura_nuvens=weather.cloud_cover,
            velocidade_vento=weather.wind_speed_10m,
            direcao_vento=weather.wind_direction_10m,
            chuva=weather.rain,
            neve=weather.snowfall
        )

        session = Session(engine)

        if session.query(City).filter(City.codigo_ibge == orm_weather.codigo_ibge).first() is None:
            session.close()
            return
        
        if session.query(Weather).filter(
            Weather.data == orm_weather.data,
            Weather.codigo_ibge == orm_weather.codigo_ibge,
            Weather.codigo_uf == orm_weather.codigo_uf
        ).first() is not None:
            session.close()
            return

        session.add(orm_weather)

        session.commit()

        session.close()
        
    
