import requests as req
import sqlite3
from csv import DictReader, DictWriter

api_key = 'CNMOQfSRJZNwsQPmCY5Kzj7K6skjJ6MVf0H7iNH9'
main_url = 'https://developers.ria.com/auto/'
api_types = {
    'search_api': 'search',
    'info_api': 'info',
    'avg_price_api': 'average_price',
}

url = main_url + 'categories/1/marks/55/models'


headers = {}
params = {'api_key': api_key}

res = req.get(url, headers=headers, params=params)
data = res.json()

with open('models.csv', 'w') as file:
    headers = ['name', 'value']
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for r in data:
        csv_writer.writerow(r)


