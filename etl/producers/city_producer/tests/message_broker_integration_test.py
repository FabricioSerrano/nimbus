from controllers.streaming_controller import StreamingController


def test_message_broker():
    controller = StreamingController()

    assert controller.connect_to_broker() == True