from flask import Flask, request
from pymongo import MongoClient
from project.config import get_config
import os
from project.health.routes import health

from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST


app = Flask(__name__)
app.register_blueprint(health)

config = get_config()
app.config.from_object(config)
dev_config= config.MONGODB_SETTINGS

client = MongoClient(dev_config['host'], dev_config['port'], username=dev_config['username'], password=dev_config['password'])
db = client['demo'] 
collection = db['data'] 

current_dir = os.path.dirname(os.path.abspath(__file__))
cert_file = os.path.join(current_dir, 'cert.pem')
key_file = os.path.join(current_dir, 'key.pem')
ssl_context = (cert_file, key_file)

REQUESTS = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint'])

@app.route('/')
def test():
    REQUESTS.labels(method='GET', endpoint='/').inc()
    return 'Hello from Flask & Docker'

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route('/add_data', methods=['POST'])
def add_data(): 
    data = request.json    
    if data:
        collection.insert_one(data)
        return 'Data added to MongoDB'
    else:
        return 'No data provided'
    

def main() -> None:
    print("Test")

if __name__ == "__main__":
    main()
    app.run(debug=True,ssl_context=(ssl_context))
