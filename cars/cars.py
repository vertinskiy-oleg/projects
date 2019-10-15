import requests as req
import sqlite3

api_key = 'CNMOQfSRJZNwsQPmCY5Kzj7K6skjJ6MVf0H7iNH9'
main_url = 'https://developers.ria.com/auto/'

years = [2010, 2011, 2012, 2013, 2014, 2015]


def write_to_sqlite(data=None):
    ###SQLite Start
    conn = sqlite3.connect('cars.db')
    c = conn.cursor()

    # c.execute('''CREATE TABLE cars_avg_prices
    #             (mark TEXT, model TEXT, year INTEGER, region TEXT, total INTEGER, 
    #           arithmeticMean REAL, interQuartileMean REAL, percentiles TEXT, prices TEXT,
    #           classifieds TEXT );''')

    # c.execute('''INSERT INTO cars_avg_price
    #             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    #             ''', ('Nissan', 'Qashqai', 2010, Kiev, data['total'], data['arithmeticMean'], 
    #                   data['interQuartileMean'], str(data['percentiles']), str(data['prices']),  
    #                   str(data['classifieds'])))

    conn.commit()
    conn.close()
    ###SQLite End

def make_request(url, headers, params):
    res = req.get(url, headers=headers, params=params)
    data = res.json()
    return write_to_sqlite(data)

def search():
    global api_key, main_url
    url = main_url + 'search'
    headers = {}
    params = {
    'api_key': api_key,
    'category_id': 1,
    'bodystyle[0]': 5,
    'state[0]': 10,
    'city[0]': 0,
    's_yers[0]': 2010,
    'price_do': 15000,
    'currency': 1,
    'type[0]': 1,
    'type[1]': 2,
    'gearbox[0]': 2,
    'gearbox[1]': 3,
    'gearbox[2]': 4,
    'gearbox[3]': 5,
    'abroad': 2,
    'custom': 1,
    'countpage': 100,
    'page': 0
    }

    return make_request(url, headers, params)

def info():
    global api_key, main_url
    url = main_url + 'info'
    headers = {}
    params = {
    'api_key': api_key,
    'auto_id': 25275604
    }

    return make_request(url, headers, params)

def avg_price():
    global api_key, main_url
    url = main_url + 'average_price'
    headers = {}
    params = {
        'api_key': api_key,
        'marka_id': 55,
        'model_id': 2197,
        'yers': 2010,
        'state_id': 10,
        'gear_id': 2,
        'custom': 0
        }

    return make_request(url, headers, params)






