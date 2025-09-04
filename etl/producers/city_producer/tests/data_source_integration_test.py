from controllers.data_controller import DataController
from schemas.city_schema import CitySchema
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_data_integration():

    data_controller = DataController()

    data = data_controller.fetch_data()

    assert data is not None

    assert isinstance(data_controller.validate_data(data[0]), CitySchema) == True
