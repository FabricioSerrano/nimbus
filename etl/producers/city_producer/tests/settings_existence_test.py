from utils.settings import Settings


def test_settings():
    settings = Settings()
    assert isinstance(settings.data_url, str) == True