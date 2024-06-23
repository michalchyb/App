from flask import Blueprint

shares = Blueprint('market', __name__, url_prefix='/market')

@shares.route('/shares')
def live():
    return 'market_test', 200