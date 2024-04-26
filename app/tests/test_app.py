from flask import Flask
from project.health.routes import health

def test_liveness_endpoint():
    app = Flask(__name__)
    app.register_blueprint(health)

    with app.test_client() as client:
        response = client.get('/health/liveness')
        assert response.status_code == 200
        assert response.data.decode('utf-8') == 'OK'

def test_readiness_endpoint():
    app = Flask(__name__)
    app.register_blueprint(health)

    with app.test_client() as client:
        response = client.get('/health/readiness')
        assert response.status_code == 200
        assert response.data.decode('utf-8') == 'OK'