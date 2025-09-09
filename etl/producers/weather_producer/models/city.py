from models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Float

class City(Base):
    __tablename__ = 'cities'
    
    
    codigo_ibge = Column(Integer, primary_key=True)
    nome_municipio = Column(String(500), nullable=False)
    capital = Column(Boolean, default=False, nullable=False)
    codigo_uf = Column(Integer, nullable=False, primary_key=True)
    uf = Column(String(2), nullable=False)
    estado = Column(String(100), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

