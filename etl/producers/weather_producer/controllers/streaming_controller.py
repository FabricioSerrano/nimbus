import json
import pika
from pika.exceptions import AMQPConnectionError
from controllers.weather_controller import WeatherController
from controllers.data_controller import DataController
from schemas.city_schema import CitySchema
from schemas.weather_schema import WeatherSchema
from pydantic import ValidationError
from utils.settings import Settings
import logging

logger = logging.getLogger('controllers.streaming_controller')


settings = Settings()
weather_controller = WeatherController()
data_controller = DataController()
connection : pika.BlockingConnection

def connect_to_broker() -> pika.BlockingConnection:
    try:

        credentials = pika.PlainCredentials(settings.mquser, settings.mqpass)
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=settings.mqhost, credentials=credentials)
        )

        logger.info('Connected to broker.')

        return connection
    
    except AMQPConnectionError:
        logger.error('Error connecting to Broker.')
        return None
    
    
def callback(ch, method, properties, body):
    try:
        data = json.loads(body)

        city = CitySchema(**data) 

        raw_weather = weather_controller.get_weather_info(city)

        weather = WeatherSchema(**raw_weather)

        data_controller.push_data(weather)

        ch.basic_ack(delivery_tag=method.delivery_tag)

    except ValidationError as e:
        logger.error(f"Validation error: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)

def listen() -> None:
    connection = connect_to_broker()

    if not isinstance(connection, pika.BlockingConnection):
        raise ConnectionError('Error connecting to message broker.')

    channel = connection.channel()
    channel.queue_declare(queue=settings.mqqueue, durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=settings.mqqueue, on_message_callback=callback)

    logger.info(f"Listening for messages on queue '{settings.mqqueue}'.")

    channel.start_consuming()
