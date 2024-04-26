from .dev import Config as DevConfig
from .prod import Config as ProdConfig

import os

def get_config():
    env = os.environ.get('FLASK_ENV', 'development')
    if env == 'production':
        return ProdConfig
    else:
        return DevConfig
