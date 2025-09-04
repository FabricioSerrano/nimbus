import logging
import requests
from typing import Iterator
from utils.settings import Settings
from schemas.city_schema import CitySchema

logger = logging.getLogger('controllers.data_controller')


class DataController:
    def __init__(self):
        pass
    
    def fetch_data(self) -> list[dict]:

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        }

        settings = Settings()

        url = settings.data_url

        response = requests.get(url, headers=headers)

        if not response.ok:
            logger.error('Data Source did not retrieved any data.')
            raise ConnectionError('Error fetching city data')
        
        
        return response.json()
        
    def validate_data(self, city : dict) -> CitySchema:

        schema = CitySchema(**city)

        return schema

    def execute(self) -> Iterator[CitySchema]:
        data = self.fetch_data()

        logger.info('Data Sucessifully retrieved.')

        for item in data:

            city = self.validate_data(item)

            logger.info(f'City {city.nome_municipio} sucessifully validated.')

            yield city

