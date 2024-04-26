from flask import Blueprint

health = Blueprint('health', __name__, url_prefix='/health')

@health.route('/liveness')
def live():
    return 'OK', 200

@health.route('/readiness')
def ready():
    return 'OK', 200