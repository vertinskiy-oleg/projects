from googleapiclient import sample_tools
from gsheets import gsheets_write, gsheets_clear

URL = 'https://testfort.com'
START_DATE = '2019-10-01'
END_DATE = '2019-10-31'

def gsc_init():
    service, flags = sample_tools.init(
        [], 'webmasters', 'v3', __doc__, __file__, parents=[],
        scope='https://www.googleapis.com/auth/webmasters.readonly')
    return service

def gsc_execute(body, url=URL):
    service = gsc_init()
    return service.searchanalytics().query(
            siteUrl=url, body=body).execute()

def gsc_get_all_queries(start_date=START_DATE, end_date=END_DATE):
    request = {
        'startDate': start_date,
        'endDate': end_date,
        'dimensions': ['query'],
        'rowLimit': 10,
        'startRow': 0
    }

    result = gsc_execute(request)
    gsheet_body = {
        'values': [
        ['Query', 'Clicks', 'Impressions', 'CTR', 'Avg. Position']
        ]
    }

    for row in result['rows']:
        gsheet_body['values'].append([row['keys'][0], row['clicks'], row['impressions'],
        round(row['ctr'] * 100, 2), round(row['position'], 2)])

    gsheets_clear(range='Sheet1')
    gsheets_write(gsheet_body, range='Sheet1')

def gsc_get_all_urls(start_date=START_DATE, end_date=END_DATE):
    request = {
        'startDate': start_date,
        'endDate': end_date,
        'dimensions': ['page'],
        'rowLimit': 10,
        'startRow': 0
    }

    result = gsc_execute(request)
    gsheet_body = {
        'values': [
        ['URL', 'Clicks', 'Impressions', 'CTR', 'Avg. Position']
        ]
    }

    for row in result['rows']:
        gsheet_body['values'].append([row['keys'][0], row['clicks'], row['impressions'],
        round(row['ctr'] * 100, 2), round(row['position'], 2)])

    gsheets_clear(range='Sheet2')
    gsheets_write(gsheet_body, range='Sheet2')

def gsc_get_all_urls_with_queries(start_date=START_DATE, end_date=END_DATE):
    request = {
        'startDate': start_date,
        'endDate': end_date,
        'dimensions': ['page', 'query'],
        'rowLimit': 1000,
        'startRow': 0
    }

    result = gsc_execute(request)
    gsheet_body = {
        'values': [
        ['URL', 'Query', 'Clicks', 'Impressions', 'CTR', 'Avg. Position']
        ]
    }

    for row in result['rows']:
        gsheet_body['values'].append([row['keys'][0], row['keys'][1], row['clicks'], row['impressions'],
        round(row['ctr'] * 100, 2), round(row['position'], 2)])

    gsheets_clear(range='Sheet3')
    gsheets_write(gsheet_body, range='Sheet3')


gsc_get_all_queries()
gsc_get_all_urls()
gsc_get_all_urls_with_queries()