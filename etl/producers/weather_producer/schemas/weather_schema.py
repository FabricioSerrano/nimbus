from typing import Annotated
from pydantic import BaseModel, Field
from datetime import datetime

class WeatherSchema(BaseModel):

    data : int
    codigo_ibge : int
    nome_municipio : str
    uf : str
    codigo_uf : int
    latitude : float
    longitude : float

    temperature_2m : float
    relative_humidity_2m : float
    wind_speed_10m : float
    wind_direction_10m : float
    cloud_cover : float
    precipitation : float
    rain : float
    snowfall : float