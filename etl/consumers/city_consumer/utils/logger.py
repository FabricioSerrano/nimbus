import os
import logging
from utils.settings import Settings


def setup_logging():
    '''Set up logging configuration.'''

    settings = Settings()

    # os.makedirs(settings.log_dir, exist_ok=True)

    logging.basicConfig(
        level=getattr(logging, settings.log_level.upper(), logging.INFO),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            # logging.FileHandler(os.path.join(settings.log_dir, 'app.log')),
            logging.StreamHandler()
        ]
    )
