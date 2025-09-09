from typing import Annotated
from pydantic import BaseModel, Field


class CitySchema(BaseModel):

    codigo_ibge : int
    nome_municipio : Annotated[str, Field(min_length=1)]
    capital : bool
    codigo_uf : int
    uf : Annotated[str, Field(min_length=2, max_length=2)]
    estado : Annotated[str, Field(min_length=1)]
    latitude : float
    longitude : float
