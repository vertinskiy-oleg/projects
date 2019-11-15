from googleapiclient import sample_tools
from gsheets import gsheets_write

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
    return result

print(gsc_get_all_queries())



# gsheet_body = {
#     'values': [
#     ['Query', 'Clicks', 'Impressions', 'CTR', 'Avg. Position']
#     ]
# }

# for row in result['rows']:
#     gsheet_body['values'].append([row['keys'][0], row['clicks'], row['impressions'], 
#         round(row['ctr'] * 100, 2), round(row['position'], 2)])

# gsheets_write(gsheet_body)
