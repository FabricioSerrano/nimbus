from controllers.data_controller import DataController
from controllers.streaming_controller import StreamingController
from utils.logger import setup_logging


def main() -> None:
    setup_logging()

    data_controller = DataController()
    streaming_controller = StreamingController()

    if not streaming_controller.connect_to_broker():
        return

    for city in data_controller.execute():
        streaming_controller.push_message(city)

    streaming_controller.close_connection()


if __name__ == '__main__':
    main()
