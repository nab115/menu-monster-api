from flask import Flask
from flask import request
import os

from utils import get_db_client
from match import get_matching_items
from menu_scraper import create_restaurant_object

env = os.environ.get('PYTHON_ENV')
app = Flask(__name__)

client = get_db_client (
    os.environ.get('MONGODB_USERNAME')
    , os.environ.get('MONGODB_PASSWORD')
)

@app.route('/')
def home():
    return { 'message': 'api endpoint for menuMonster'}

@app.route('/itemsearch', methods=['POST'])
def menu_item_search():
    db = client['Restaurants']
    col = db['restaurants']

    try:
        city = request.json['city']
        item = request.json['item']
    except:
        print('Bad Request : city and or item not sent')

    restaurants = col.find({'city': city}, {'_id': False})

    return get_matching_items(restaurants, item)

@app.route('/locations', methods=['GET'])
def get_locations():
    db = client['Restaurants']
    col = db['restaurants']

    cities = col.distinct('city')

    return sorted(cities)

@app.route('/locationsearch', methods=['POST'])
def location_search():
    db = client['Restaurants']
    col = db['restaurants']

    try:
        city = request.json['city']
    except:
        print('Bad Request : city not sent')

    restaurants = col.find({'city': city}, {'_id': False})
    return [r for r in restaurants]

@app.route('/scraper', methods=['POST'])
def scraper():
    db = client['Restaurants']
    col = db['restaurants']

    try: 
        url = request.json['url']
    except:
        return 'Bad Request, url not sent', 400

    try:
        restaurant = create_restaurant_object(url, url, '', '')
        return restaurant
    except:
        print('Error parsing ' + url)
        return f'Error parsing {url}', 400

if __name__ == '__main__':
    if (env == 'development'):
        app.run(port=5000)
    else:
        from waitress import serve
        serve(app, host='0.0.0.0', port = os.environ.get('PORT'))