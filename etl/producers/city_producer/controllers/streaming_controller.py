import pika
from pika.exceptions import AMQPConnectionError
from pika.channel import Channel
from schemas.city_schema import CitySchema
from utils.settings import Settings
import logging

logger = logging.getLogger('controllers.streaming_controller')

class StreamingController:
    def __init__(self):
        self.settings = Settings()
        self.connection : pika.BlockingConnection
        self.channel : Channel
    
    def connect_to_broker(self) -> bool:
        
        try:

            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=self.settings.mqhost)
            )

            logger.info('Connected to broker.')

            self.channel = self.connection.channel()
            self.channel.queue_declare(queue=self.settings.mqqueue, durable=True)

            return True
        
        except AMQPConnectionError as er:
            logger.error(f'Error connecting to Broker. {er}')
            return False


    def push_message(self, city : CitySchema) -> None:

        if self.connection is None:
            raise ConnectionError('Error connecting to broker')

        self.channel.basic_publish(
            exchange='',
            routing_key=self.settings.mqqueue,
            body=city.model_dump_json(),
            properties=pika.BasicProperties(delivery_mode=2)
        )

        

    def close_connection(self) -> None:
        self.channel.close()
        self.connection.close()


