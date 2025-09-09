from models.base import Base
from models.city import City
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKeyConstraint


class Weather(Base):
    __tablename__ = 'weathers'
    
    
    data = Column(DateTime, primary_key=True)
    codigo_ibge = Column(Integer, primary_key=True)
    codigo_uf = Column(Integer, primary_key=True)
    nome_municipio = Column(String(500), nullable=False)
    uf = Column(String(2), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    temperatura = Column(Float, nullable=False)
    humidade_relativa = Column(Float, nullable=False)
    precipitacao = Column(Float, nullable=False)
    cobertura_nuvens = Column(Float, nullable=False)
    velocidade_vento = Column(Float, nullable=False)
    direcao_vento = Column(Float, nullable=False)
    chuva = Column(Float, nullable=False)
    neve = Column(Float, nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(
            ['codigo_ibge', 'codigo_uf'],
            ['cities.codigo_ibge', 'cities.codigo_uf']
        ),
    )

