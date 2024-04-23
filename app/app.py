from flask import Flask
from automations.file_remover import remove_files
from pymongo import MongoClient
from config import get_config
import os

app = Flask(__name__)

config = get_config()
app.config.from_object(config)
dev_config= config.MONGODB_SETTINGS

client = MongoClient(dev_config['host'], dev_config['port'], username=dev_config['username'], password=dev_config['password'])
db = client['demo'] 
collection = db['data'] 

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'

@app.route('/add_data', methods=['', 'POST'])
def add_data(): 
    data = {
            "logo": "John",
            "age": 30
        }
    
    if data:
        collection.insert_one(data)
        return 'Data added to MongoDB'
    else:
        return 'No data provided'
    

def main():
    print("Test")

if __name__ == "__main__":
    app.run(debug=True,ssl_context=('cert.pem', 'key.pem'))