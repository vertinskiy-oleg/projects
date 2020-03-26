from play_scraper import search as gp_search
from csv import writer
from random import randint
from time import sleep

queries = ['messenger', 'chat', 'conference', 'cloud meeting',
           'videochat', 'skype', 'viber', 'hangouts', 'slack']

with open('apps.csv', 'w', encoding="utf-8", newline='') as f:
    csv_writer = writer(f)
    csv_writer.writerow(['Title', 'App Id', 'URL', 'Category', 'Developer', 'Developer Email',
                         'Developer URL', 'Installs', 'Reviews', 'Score', 'Price', 'Updated', 'Icon', 'Screenshots'])


def run_search(query):
    search_apps = gp_search(query, detailed=True)

    with open('apps.csv', 'a', encoding="utf-8", newline='') as f:
        csv_writer = writer(f)

        for app in search_apps:
            if app['reviews'] > 100:
                if float(app['score']) < 2.8 or float(app['score']) > 4.2:
                    continue
                csv_writer.writerow(
                    [app['title'], app['app_id'], app['url'], app['category'],
                     app['developer'], app['developer_email'], app['developer_url'],
                     app['installs'], app['reviews'], app['score'], app['price'],
                     app['updated'], app['icon'], app['screenshots']])


for query in queries:
    print(f'Running search: {query}')
    run_search(query)
    sleep_time = randint(0, 10)
    print(f'Sleeping for: {sleep_time}')
    sleep(sleep_time)
