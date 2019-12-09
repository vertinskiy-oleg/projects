#Сделать таблицу с Страна - URL - Запрос with Ukraine & India
#Add Ukraine & India to Countries table
#Make code refactoring
from googleapiclient import sample_tools
from gsheets import gsheets_write, gsheets_clear

URL = 'https://testfort.com'
START_DATE = '2019-10-01'
END_DATE = '2019-10-31'
ROW_LIMIT = 3

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

#General function for requesting GSC with parameters
# Dimensions: query, page, country, device, date
# Filters: no_ukr, no_ind, no_blog, only_blog
def gsc_make_request(dimensions=['query'], filter=[]):
    
    filters = {
        'no_ukr': {
                "dimension": "country",
                "operator": "notContains",
                "expression": "ukr"
                },
        'no_ind': {
                "dimension": "country",
                "operator": "notContains",
                "expression": "ind"
                },
        'no_blog': {
                "dimension": "page",
                "operator": "notContains",
                "expression": "blog"
                },
        'only_blog': {
                "dimension": "page",
                "operator": "contains",
                "expression": "blog"
                }
    }
    
    request = {
        'startDate': START_DATE,
        'endDate': END_DATE,
        'dimensions': dimensions,
        'rowLimit': ROW_LIMIT,
        'startRow': 0,
        "dimensionFilterGroups": [
            {
            "filters": [filters[f] for f in filter]
            }
        ]
    }

    result = gsc_execute(request)
    gsc_write_to_gsheets(dimensions, result)


#General function for writing GSC data to GSheets
#Sheets: LP Queries, Blog Queries, LP URL, Blog URL, LP URL-Query, 
#Blog URL-Query, LP-Countries, Blog-Countries
def gsc_write_to_gsheets(dimensions, result, sheet='Sheet1'):

    gsheet_body = {
        'values': [
        ['Date', *dimensions, 'Clicks', 'Impressions', 'CTR', 'Avg. Position']
        ]
    }

    for row in result['rows']:
        gsheet_body['values'].append([START_DATE, *row['keys'], row['clicks'], 
        row['impressions'], round(row['ctr'] * 100, 2), round(row['position'], 2)])

    print(gsheet_body)
    # gsheets_clear(range=sheet)
    # gsheets_write(gsheet_body, range=sheet)


gsc_make_request(dimensions=['query'], filter=[])
