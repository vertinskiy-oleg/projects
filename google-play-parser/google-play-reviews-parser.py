from google_play_scraper import Sort, reviews as gp_reviews
from csv import reader, writer
from random import randint
from time import sleep

apps = []

with open('apps.csv', 'r', encoding="utf-8") as f:
    csv_reader = reader(f)
    csv_reader.__next__()
    for row in csv_reader:
        apps.append(row[1])

with open('negative_reviews.csv', 'w', encoding="utf-8", newline='') as f:
    csv_writer = writer(f)
    csv_writer.writerow(['App', 'Date', 'Review Content', 'Score', 'Thumbs Up', 'Reply Content'])


def get_bad_reviews(app):
    app_reviews = gp_reviews(
        app,
        lang='en',
        country='us',
        sort=Sort.MOST_RELEVANT,
        count=100,
        filter_score_with=1
    )

    with open('negative_reviews.csv', 'a', encoding="utf-8", newline='') as f:
        csv_writer = writer(f)

        for review in app_reviews:
            csv_writer.writerow([
                app,
                review['at'], review['content'],
                review['score'], review['thumbsUpCount'],
                review['replyContent']
            ])


for app in apps:
    print(f'Collecting reviews from: {app}')
    try:
        get_bad_reviews(app)
    except Exception as e:
        continue
    sleep_time = randint(0, 10)
    print(f'Sleeping for: {sleep_time}')
    sleep(sleep_time)
