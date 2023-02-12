from flask import Flask
from flask import request
import os

from utils import get_db_client

port = os.environ.get('PORT') if os.environ.get('PORT') else 5000

app = Flask(__name__)

client = get_db_client (
    os.environ.get('MONGODB_USERNAME')
    , os.environ.get('MONGODB_PASSWORD')
)

@app.route('/')
def home():
    return { message: 'api endpoint for menuMonster'}

@app.route('/api/itemsearch', methods=['Get', 'POST'])
def menu_item_search():
    db = client['Restaurants']
    col = db['restaurants']

    if request.method == 'POST':
        print(request.json['city'])
    
    restaurant = col.find_one({}, {'_id': False})

    return restaurant

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)