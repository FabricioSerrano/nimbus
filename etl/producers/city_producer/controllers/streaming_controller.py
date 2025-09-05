import pika
from pika.exceptions import AMQPConnectionError
from schemas.city_schema import CitySchema
from utils.settings import Settings
import logging

logger = logging.getLogger('controllers.streaming_controller')

class StreamingController:
    def __init__(self):
        self.settings = Settings()
        self.connection : pika.BlockingConnection
    
    def connect_to_broker(self) -> bool:
        
        try:

            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=self.settings.mqhost)
            )

            logger.info('Connected to broker.')

            return True
        
        except AMQPConnectionError:
            logger.error('Error connecting to Broker.')
            return False


    def push_message(self, city : CitySchema) -> None:

        if self.connection is None:
            raise ConnectionError('Error connecting to broker')
        
        channel = self.connection.channel()

        channel.queue_declare(queue=self.settings.mqqueue, durable=True)

        channel.basic_publish(
            exchange='',
            routing_key=self.settings.mqqueue,
            body=city.model_dump_json(),
            properties=pika.BasicProperties(delivery_mode=2)
        )

        channel.close()

    def close_connection(self) -> None:
        self.connection.close()


