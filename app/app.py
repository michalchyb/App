from flask import Flask, request
from pymongo import MongoClient
from project.config import get_config
from project.health.routes import health
from project.config.ssl_config import SSLConfig

from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST


app = Flask(__name__)
app.register_blueprint(health)

config = get_config()
app.config.from_object(config)
dev_config= config.MONGODB_SETTINGS

client = MongoClient(dev_config['host'], dev_config['port'], username=dev_config['username'], password=dev_config['password'])
db = client['demo'] 
collection = db['data'] 

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
    ssl_config = SSLConfig()
    ssl_context = ssl_config.get_ssl_context()
    app.run(debug=True,ssl_context=(ssl_context))
