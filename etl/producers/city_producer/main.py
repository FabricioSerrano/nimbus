from controllers.data_controller import DataController
from controllers.streaming_controller import StreamingController
from utils.logger import setup_logging


if __name__ == '__main__':

    setup_logging()

    data_controller = DataController()
    streaming_controller = StreamingController()

    streaming_controller.connect_to_broker()

    for city in data_controller.execute():
        streaming_controller.push_message(city)

    streaming_controller.close_connection()
