#Сделать таблицу с Страна - URL - Запрос with Ukraine & India
#Add Ukraine & India to Countries table
#Optimize functions with dict.copy() and diff function parameters
from googleapiclient import sample_tools
from gsheets import gsheets_write, gsheets_clear

URL = 'https://testfort.com'
START_DATE = '2019-10-01'
END_DATE = '2019-10-31'

#GSC API Authorization
def gsc_init():
    service, flags = sample_tools.init(
        [], 'webmasters', 'v3', __doc__, __file__, parents=[],
        scope='https://www.googleapis.com/auth/webmasters.readonly')
    return service

#Executing API queries
def gsc_execute(body, url=URL):
    service = gsc_init()
    return service.searchanalytics().query(
            siteUrl=url, body=body).execute()

#Getting gueries whithout Ukraine & India excluding /blog
def gsc_get_lp_queries(start_date=START_DATE, end_date=END_DATE):
    request = {
        'startDate': start_date,
        'endDate': end_date,
        'dimensions': ['query'],
        'rowLimit': 1000,
        'startRow': 0,
        "dimensionFilterGroups": [
            {
            "filters": [
                {
                "dimension": "country",
                "operator": "notContains",
                "expression": "ukr"
                },
                {
                "dimension": "country",
                "operator": "notContains",
                "expression": "ind"
                },
                {
                "dimension": "page",
                "operator": "notContains",
                "expression": "blog"
                }
            ]
            }
        ]
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

    gsheets_clear(range='LP Queries')
    gsheets_write(gsheet_body, range='LP Queries')

#Getting gueries whithout Ukraine & India only /blog
def gsc_get_blog_queries(start_date=START_DATE, end_date=END_DATE):
    request = {
        'startDate': start_date,
        'endDate': end_date,
        'dimensions': ['query'],
        'rowLimit': 1000,
        'startRow': 0,
        "dimensionFilterGroups": [
            {
            "filters": [
                {
                "dimension": "country",
                "operator": "notContains",
                "expression": "ukr"
                },
                {
                "dimension": "country",
                "operator": "notContains",
                "expression": "ind"
                },
                {
                "dimension": "page",
                "operator": "contains",
                "expression": "blog"
                }
            ]
            }
        ]
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

    gsheets_clear(range='Blog Queries')
    gsheets_write(gsheet_body, range='Blog Queries')

#Getting urls whithout Ukraine & India excluding /blog
def gsc_get_lp_urls(start_date=START_DATE, end_date=END_DATE):
    request = {
        'startDate': start_date,
        'endDate': end_date,
        'dimensions': ['page'],
        'rowLimit': 1000,
        'startRow': 0,
        "dimensionFilterGroups": [
            {
            "filters": [
                {
                "dimension": "country",
                "operator": "notContains",
                "expression": "ukr"
                },
                {
                "dimension": "country",
                "operator": "notContains",
                "expression": "ind"
                },
                 {
                "dimension": "page",
                "operator": "notContains",
                "expression": "blog"
                }
            ]
            }
        ]
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

    gsheets_clear(range='LP URL')
    gsheets_write(gsheet_body, range='LP URL')

#Getting urls whithout Ukraine & India only /blog
def gsc_get_blog_urls(start_date=START_DATE, end_date=END_DATE):
    request = {
        'startDate': start_date,
        'endDate': end_date,
        'dimensions': ['page'],
        'rowLimit': 1000,
        'startRow': 0,
        "dimensionFilterGroups": [
            {
            "filters": [
                {
                "dimension": "country",
                "operator": "notContains",
                "expression": "ukr"
                },
                {
                "dimension": "country",
                "operator": "notContains",
                "expression": "ind"
                },
                 {
                "dimension": "page",
                "operator": "contains",
                "expression": "blog"
                }
            ]
            }
        ]
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

    gsheets_clear(range='Blog URL')
    gsheets_write(gsheet_body, range='Blog URL')

#Getting countries whithout Ukraine & India excluding /blog
def gsc_get_lp_countries(start_date=START_DATE, end_date=END_DATE):
    request = {
        'startDate': start_date,
        'endDate': end_date,
        'dimensions': ['country'],
        'rowLimit': 1000,
        'startRow': 0,
        "dimensionFilterGroups": [
            {
            "filters": [
                {
                "dimension": "country",
                "operator": "notContains",
                "expression": "ukr"
                },
                {
                "dimension": "country",
                "operator": "notContains",
                "expression": "ind"
                },
                {
                "dimension": "page",
                "operator": "notContains",
                "expression": "blog"
                }
            ]
            }
        ]
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

    gsheets_clear(range='LP-Countries')
    gsheets_write(gsheet_body, range='LP-Countries')

#Getting countries whithout Ukraine & India only /blog
def gsc_get_blog_countries(start_date=START_DATE, end_date=END_DATE):
    request = {
        'startDate': start_date,
        'endDate': end_date,
        'dimensions': ['country'],
        'rowLimit': 1000,
        'startRow': 0,
        "dimensionFilterGroups": [
            {
            "filters": [
                {
                "dimension": "country",
                "operator": "notContains",
                "expression": "ukr"
                },
                {
                "dimension": "country",
                "operator": "notContains",
                "expression": "ind"
                },
                {
                "dimension": "page",
                "operator": "notContains",
                "expression": "blog"
                }
            ]
            }
        ]
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

    gsheets_clear(range='Blog-Countries')
    gsheets_write(gsheet_body, range='Blog-Countries')

#Getting urls & queries whithout Ukraine & India excluding /blog
def gsc_get_lp_urls_with_queries(start_date=START_DATE, end_date=END_DATE):
    request = {
        'startDate': start_date,
        'endDate': end_date,
        'dimensions': ['page', 'query'],
        'rowLimit': 1000,
        'startRow': 0,
        "dimensionFilterGroups": [
            {
            "filters": [
                {
                "dimension": "page",
                "operator": "notContains",
                "expression": "blog"
                }
            ]
            }
        ]
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

    gsheets_clear(range='LP URL-Query')
    gsheets_write(gsheet_body, range='LP URL-Query')

#Getting urls & queries whithout Ukraine & India only /blog
def gsc_get_blog_urls_with_queries(start_date=START_DATE, end_date=END_DATE):
    request = {
        'startDate': start_date,
        'endDate': end_date,
        'dimensions': ['page', 'query'],
        'rowLimit': 1000,
        'startRow': 0,
        "dimensionFilterGroups": [
            {
            "filters": [
                {
                "dimension": "page",
                "operator": "contains",
                "expression": "blog"
                }
            ]
            }
        ]
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

    gsheets_clear(range='Blog URL-Query')
    gsheets_write(gsheet_body, range='Blog URL-Query')

gsc_get_lp_queries()
gsc_get_blog_queries()
gsc_get_lp_urls()
gsc_get_blog_urls()
gsc_get_lp_countries()
gsc_get_blog_countries()
gsc_get_lp_urls_with_queries()
gsc_get_blog_urls_with_queries()