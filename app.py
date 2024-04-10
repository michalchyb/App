from flask import Flask
from automations.file_remover import remove_files
from pymongo import MongoClient
import config

app = Flask(__name__)

client = MongoClient(config.host, config.port, username=config.username, password=config.password)
db = client['demo'] 
collection = db['data'] 

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'

@app.route('/add_data', methods=['GET', 'POST'])
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
    app.run(debug=True)