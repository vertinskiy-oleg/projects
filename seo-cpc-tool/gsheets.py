from googleapiclient import sample_tools

SPREADSHEET_ID = '1Yit1pyDj6Mv3NmccWJ-XVuxLhAGcKFwg5-Vl7tG1bUY'
RANGE_NAME = 'Sheet1'

def gsheet_init():
    service, flags = sample_tools.init(
        [], 'sheets', 'v4', __doc__, __file__, parents=[],
        scope='https://www.googleapis.com/auth/spreadsheets')
    return service.spreadsheets()

def gsheets_write(body, id=SPREADSHEET_ID, range=RANGE_NAME):
    s = gsheet_init()
    s.values().update(
        spreadsheetId=id, range=range,
        valueInputOption='RAW', body=body).execute()

def gsheets_clear(id=SPREADSHEET_ID, range=RANGE_NAME):
    s = gsheet_init()
    s.values().clear(
        spreadsheetId=id, range=range).execute()
