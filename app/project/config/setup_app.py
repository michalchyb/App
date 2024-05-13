from flask import Flask
from pymongo import MongoClient
from project.config import get_config


def setup_app():
    app = Flask(__name__)
    
    # setup profile
    config = get_config()
    app.config.from_object(config)
    
    dev_config= config.MONGODB_SETTINGS
    client = MongoClient(dev_config['host'], dev_config['port'], username=dev_config['username'], password=dev_config['password'])
    db = client['demo'] 
    collection = db['data'] 
    
    return app, collection, config

