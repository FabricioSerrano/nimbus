from pydantic import BaseModel


class CitySchema(BaseModel):

    codigo_ibge : int
    nome_municipio : str
    capital : bool
    codigo_uf : int
    uf : str
    estado : str
    latitude : float
    longitude : float
