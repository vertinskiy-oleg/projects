import requests as req
import sqlite3

api_key = 'CNMOQfSRJZNwsQPmCY5Kzj7K6skjJ6MVf0H7iNH9'
main_url = 'https://developers.ria.com/auto/'

#SQLite Start
# def write_to_sqlite(avg_price_info=None, data=None):

#     conn = sqlite3.connect('cars.db')
#     c = conn.cursor()

#     # c.execute('''CREATE TABLE cars_avg_prices
#     #             (id INTEGER, mark TEXT, model TEXT, year INTEGER, region TEXT, total INTEGER, 
#     #           arithmeticMean REAL, interQuartileMean REAL, percentiles TEXT, prices TEXT,
#     #           classifieds TEXT );''')

#     c.execute('''INSERT INTO cars_avg_prices
#                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
#                 ''', (avg_price_info['mark'], avg_price_info['model'], avg_price_info['year'], 
#                     avg_price_info['region'], data['total'], data['arithmeticMean'], 
#                     data['interQuartileMean'], str(data['percentiles']), str(data['prices']),  
#                     str(data['classifieds'])))

#     conn.commit()
#     conn.close()
#SQLite End

#Request Block Start
def make_request(url, headers, params):
    res = req.get(url, headers=headers, params=params)
    data = res.json()
    return data
#Request Block End

#Info Block Start
# def info(id):
#     global api_key, main_url
#     url = main_url + 'info'
#     headers = {}
#     params = {
#     'api_key': api_key,
#     'auto_id': id
#     }

#     data = make_request(url, headers, params)
#     id_info = {
#         'mark': data['markName'],
#         'model': data['modelName'],
#         'year': data['autoData']['year'],
#         'region': data['locationCityName'],
#         'price': data['USD'],
#         'version': data['autoData']['version'],
#         'race': data['autoData']['race'],
#         'fuel': data['autoData']['fuelName'],
#         'gear_box': data['autoData']['gearboxName'],
#         'VIN': data['VIN'],
#         'add_date': data['addDate'],
#         'update_date': data['updateDate'],
#         'url': 'https://auto.ria.com' + data['linkToView'],
#         'description': data['autoData']['description']
#     }
#     return id_info

# print(info(24814679))
#Info Block End

#Search Ids Block Start
# def search(page):
#     global api_key, main_url, ids
#     url = main_url + 'search'
#     headers = {}
#     params = {
#     'api_key': api_key,
#     'category_id': 1,
#     'bodystyle[0]': 5,
#     'state[0]': 10,
#     'city[0]': 0,
#     's_yers[0]': 2010,
#     'price_do': 15000,
#     'currency': 1,
#     'type[0]': 1,
#     'type[1]': 2,
#     'gearbox[0]': 2,
#     'gearbox[1]': 3,
#     'gearbox[2]': 4,
#     'gearbox[3]': 5,
#     'abroad': 2,
#     'custom': 1,
#     'damage': 0,
#     'countpage': 100,
#     'page': page
#     }
    
#     data = make_request(url, headers, params)
#     ids.extend(data['result']['search_result']['ids'])

#     return data['result']['search_result']['count']

# ids = []
# count = search(0)
# i = 1
# while len(ids) < count:
#     search(i)
#     i += 1

#Search Ids Block End

#Average Price Block Start
# def avg_price(mark, model, year, region):
#     global api_key, main_url
#     url = main_url + 'average_price'
#     headers = {}
#     params = {
#         'api_key': api_key,
#         'marka_id': marks[mark],
#         'model_id': models[model],
#         'yers': year,
#         'state_id': regions[region],
#         'gear_id': 2,
#         'custom': 0
#         }
#     avg_price_info = {
#         'mark': mark, 
#         'model': model,
#         'year': year,
#         'region': region
#         }
#     return write_to_sqlite(avg_price_info, make_request(url, headers, params))

# years = [2010, 2011, 2012, 2013, 2014, 2015]

# marks = {
#     'Ford': 24,
#     'Nissan': 55,
#     'Mitsubishi': 52,
#     'Honda': 28,
#     'Hyundai': 29,
#     'Kia': 33,
#     'Mazda': 47,
#     'Opel': 56,
#     'Subaru': 75,
#     'Suzuki': 76,
#     'Toyota': 79,
#     'Volkswagen': 84,
#     'SsangYong': 73
# }

# models = {
#     'Kuga': 2874,
#     'Qashqai': 2197,
#     'X-Trail': 507,
#     'ASX': 30805,
#     'Outlander': 1485,
#     'CR-V': 269,
#     'IX35': 3901,
#     'Tucson': 1268,
#     'Santa FE': 293,
#     'Sportage': 327,
#     'Sorento': 326,
#     'CX-5': 37381,
#     'Mokka': 42885,
#     'Forester': 663,
#     'Outback': 1720,
#     'XV': 38372,
#     'Grand Vitara': 672,
#     'RAV4': 715,
#     'Tiguan': 2692,
#     'Korando': 658
# }

# regions = {
#     'Kiev': 10
# }

# for y in years:
#     avg_price('SsangYong', 'Korando', y, 'Kiev')
#Average Price Block End






