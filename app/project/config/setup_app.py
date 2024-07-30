from flask import Flask
from pymongo import MongoClient
from project.health.routes import health
from project.market.shares import shares
from project.iot.iots import iot
from pymongo.errors import ServerSelectionTimeoutError
from project.config import get_config


def setup_app():
    app = Flask(__name__)
    
    # Setup configuration
    config = get_config()
    app.config.from_object(config)
    
    # Initialize database
    client = init_db(config)
    db = client['demo']
    app.config['db'] = db
    
    
    # Register blueprints
    register_blueprints(app)
    
    return app, db


def init_db(config):
    try:
        config = config.MONGODB_SETTINGS
        client = MongoClient(
            config['host'], 
            config['port'], 
            username=config.get('username'), 
            password=config.get('password')
        )
        client.server_info()
        return client
    except ServerSelectionTimeoutError as e:
        print(f"MongoDB connection timed out: {e}")
        raise
    

def register_blueprints(app):
    app.register_blueprint(health)
    app.register_blueprint(shares)
    app.register_blueprint(iot)