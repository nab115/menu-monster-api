from flask import Flask
from flask import request
import os

from utils import get_db_client

app = Flask(__name__)

client = get_db_client (
    os.environ.get('MONGODB_USERNAME')
    , os.environ.get('MONGODB_PASSWORD')
)

@app.route('/api/itemsearch', methods=['POST'])
def menu_item_search():
    db = client['Restaurants']
    col = db['restaurants']

    if request.method == 'POST':
        print(request.json['city'])
    
    restaurant = col.find_one({}, {'_id': False})
    print('asuhdude')

    return restaurant

if __name__ == '__main__':
    app.run(port=5000)