import openmeteo_requests
import requests_cache
from retry_requests import retry
from datetime import datetime
from utils.settings import Settings
from schemas.city_schema import CitySchema
import logging

logger = logging.getLogger('controllers.weather_controller')


class WeatherController:
	def __init__(self):
		self.cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
		self.retry_session = retry(self.cache_session, retries = 5, backoff_factor = 0.2)
		self.openmeteo = openmeteo_requests.Client(session = self.retry_session)
		self.settings = Settings()

	def get_weather_info(self, city : CitySchema) -> dict[str, str | int | float]:

		data_info = ["temperature_2m", "relative_humidity_2m", "wind_speed_10m", "wind_direction_10m", "cloud_cover", "precipitation", "rain", "snowfall"]

		params = {
			"latitude": city.latitude,
			"longitude": city.longitude,
			"current": data_info,
			"timezone": "America/Sao_Paulo"
		}


		responses = self.openmeteo.weather_api(self.settings.openmeteourl, params=params)

		response = responses[0]

		current_data = response.Current()

		city_weather_data = {}

		city_weather_data['data'] = current_data.Time()
		city_weather_data['codigo_ibge'] = city.codigo_ibge
		city_weather_data['nome_municipio'] = city.nome_municipio
		city_weather_data['uf'] = city.uf
		city_weather_data['codigo_uf'] = city.codigo_uf
		city_weather_data['latitude'] = city.latitude
		city_weather_data['longitude'] = city.longitude 

		for index, header in enumerate(data_info):
			city_weather_data[header] = current_data.Variables(index).Value()


		return city_weather_data
