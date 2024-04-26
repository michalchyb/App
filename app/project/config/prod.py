
import os

class Config:
    DEBUG = False
    MONGODB_SETTINGS = {
        'host': 'mongodb-service',
        'port': 27017,
        'username': os.environ.get('MONGO_USER', ''),
        'password': os.environ.get('MONGO_PASSWORD', '')
    }