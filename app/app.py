from project.config.setup_app import setup_app
from project.health.routes import health
from project.config.ssl_config import SSLConfig

from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app, config = setup_app()

REQUESTS = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint'])

@app.route('/')
def test():
    REQUESTS.labels(method='GET', endpoint='/').inc()
    return 'Hello from Flask & Docker'

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}    

def main() -> None:
    print("Test")

if __name__ == "__main__":
    main()
    ssl_config = SSLConfig()
    ssl_context = ssl_config.get_ssl_context()
    app.run(debug=True,ssl_context=(ssl_context))
