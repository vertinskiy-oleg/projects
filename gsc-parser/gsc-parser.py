#Make code refactoring
from googleapiclient import sample_tools
from gsheets import gsheets_write, gsheets_clear
import datetime
import calendar

#GSC API Authorization
def gsc_init():
    service, flags = sample_tools.init(
        [], 'webmasters', 'v3', __doc__, __file__, parents=[],
        scope='https://www.googleapis.com/auth/webmasters.readonly')
    return service

#Executing API queries
def gsc_execute(body, url):
    service = gsc_init()
    return service.searchanalytics().query(
            siteUrl=url, body=body).execute()

#General function for requesting GSC with parameters
# Dimensions: query, page, country, device, date
# Filters: no_ukr, no_ind, no_blog, only_blog
def gsc_make_request(url, start_date, end_date, 
                    limit, dimensions, filters, sheet):
    
    filters_lookup = {
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
        'startDate': start_date,
        'endDate': end_date,
        'dimensions': dimensions,
        'rowLimit': limit,
        'startRow': 0,
        "dimensionFilterGroups": [
            {
            "filters": [filters_lookup[f] for f in filters]
            }
        ]
    }

    result = gsc_execute(request, url)
    gsc_write_to_gsheets(start_date, dimensions, result, sheet)


#General function for writing GSC data to GSheets
#Sheets: LP Queries, Blog Queries, LP URL, Blog URL, LP URL-Query, 
#Blog URL-Query, LP-Countries, Blog-Countries
def gsc_write_to_gsheets(date, dimensions, result, sheet):

    gsheet_body = {
        'values': [
        ['Date', *dimensions, 'Clicks', 'Impressions', 'CTR', 'Avg. Position']
        ]
    }

    for row in result['rows']:
        gsheet_body['values'].append([date, *row['keys'], row['clicks'], 
        row['impressions'], round(row['ctr'] * 100, 2), round(row['position'], 2)])

    #gsheets_clear(range=sheet)
    gsheets_write(gsheet_body, range=sheet)


qarea = 'https://qarea.com'
testfort = 'https://testfort.com'

#Main function:
def main(url=qarea, year=2019, months=[1], limit=10, 
                    dimensions=['query'], filters=[], sheet='Sheet1'):

    if len(months) == 1:
        start_date = str(datetime.date(year, months[0], 1))
        end_date = str(datetime.date(year, months[0], calendar.monthrange(year, months[0])[1]))
        gsc_make_request(url, start_date, end_date, limit, dimensions, filters, sheet)
    else:
        for month in months:
            start_date = str(datetime.date(year, month, 1))
            end_date = str(datetime.date(year, month, calendar.monthrange(year, month)[1]))
            gsc_make_request(url, start_date, end_date, limit, dimensions, filters, sheet)


main(url=testfort, year=2019, months=[1,2,3,4,5,6,7,8,9,10,11,12], limit=10, 
    dimensions=['page'], filters=['no_blog'], sheet='Sheet1')
