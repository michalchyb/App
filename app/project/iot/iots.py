from flask import Blueprint, current_app
from flask import request

iot = Blueprint('iot', __name__, url_prefix='/iot')

@iot.route('/temperature', methods=['POST'])
def add_data(): 
    data = request.json 
    db = current_app.config['db']   
    if data:
        db['data'].insert_one(data)
        return 'Data added to MongoDB', 201
    return 'No data provided', 400