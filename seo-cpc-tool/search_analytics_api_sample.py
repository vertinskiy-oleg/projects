from __future__ import print_function

import argparse
import sys
from googleapiclient import sample_tools

# Declare command-line flags.
argparser = argparse.ArgumentParser(add_help=False)
argparser.add_argument('property_uri', type=str,
                       help=('Site or app URI to query data for (including '
                             'trailing slash).'))
argparser.add_argument('start_date', type=str,
                       help=('Start date of the requested date range in '
                             'YYYY-MM-DD format.'))
argparser.add_argument('end_date', type=str,
                       help=('End date of the requested date range in '
                             'YYYY-MM-DD format.'))


def main(argv):
  service, flags = sample_tools.init(
      argv, 'webmasters', 'v3', __doc__, __file__, parents=[argparser],
      scope='https://www.googleapis.com/auth/webmasters.readonly')

  # First run a query to learn which dates we have data for. You should always
  # check which days in a date range have data before running your main query.
  # This query shows data for the entire range, grouped and sorted by day,
  # descending; any days without data will be missing from the results.
  request = {
      'startDate': flags.start_date,
      'endDate': flags.end_date,
      'dimensions': ['date']
  }
  response = execute_request(service, flags.property_uri, request)
  print_table(response, 'Available dates')

  # Get totals for the date range.
  request = {
      'startDate': flags.start_date,
      'endDate': flags.end_date
  }
  response = execute_request(service, flags.property_uri, request)
  print_table(response, 'Totals')

  # Get top 10 queries for the date range, sorted by click count, descending.
  request = {
      'startDate': flags.start_date,
      'endDate': flags.end_date,
      'dimensions': ['query'],
      'rowLimit': 10
  }
  response = execute_request(service, flags.property_uri, request)
  print_table(response, 'Top Queries')

  # Get top 11-20 mobile queries for the date range, sorted by click count, descending.
  request = {
      'startDate': flags.start_date,
      'endDate': flags.end_date,
      'dimensions': ['query'],
      'dimensionFilterGroups': [{
          'filters': [{
              'dimension': 'device',
              'expression': 'mobile'
          }]
      }],
      'rowLimit': 10,
      'startRow': 10
  }
  response = execute_request(service, flags.property_uri, request)
  print_table(response, 'Top 11-20 Mobile Queries')

  # Get top 10 pages for the date range, sorted by click count, descending.
  request = {
      'startDate': flags.start_date,
      'endDate': flags.end_date,
      'dimensions': ['page'],
      'rowLimit': 10
  }
  response = execute_request(service, flags.property_uri, request)
  print_table(response, 'Top Pages')

  # Get the top 10 queries in India, sorted by click count, descending.
  request = {
      'startDate': flags.start_date,
      'endDate': flags.end_date,
      'dimensions': ['query'],
      'dimensionFilterGroups': [{
          'filters': [{
              'dimension': 'country',
              'expression': 'ind'
          }]
      }],
      'rowLimit': 10
  }
  response = execute_request(service, flags.property_uri, request)
  print_table(response, 'Top queries in India')

  # Group by both country and device.
  request = {
      'startDate': flags.start_date,
      'endDate': flags.end_date,
      'dimensions': ['country', 'device'],
      'rowLimit': 10
  }
  response = execute_request(service, flags.property_uri, request)
  print_table(response, 'Group by country and device')

  # Group by total number of Search Appearance count.
  # Note: It is not possible to use searchAppearance with other
  # dimensions.
  request = {
      'startDate': flags.start_date,
      'endDate': flags.end_date,
      'dimensions': ['searchAppearance'],
      'rowLimit': 10
  }
  response = execute_request(service, flags.property_uri, request)
  print_table(response, 'Search Appearance Features')

def execute_request(service, property_uri, request):
  """Executes a searchAnalytics.query request.
  Args:
    service: The webmasters service to use when executing the query.
    property_uri: The site or app URI to request data for.
    request: The request to be executed.
  Returns:
    An array of response rows.
  """
  return service.searchanalytics().query(
      siteUrl=property_uri, body=request).execute()


def print_table(response, title):
  """Prints out a response table.
  Each row contains key(s), clicks, impressions, CTR, and average position.
  Args:
    response: The server response to be printed as a table.
    title: The title of the table.
  """
  print('\n --' + title + ':')
  
  if 'rows' not in response:
    print('Empty response')
    return

  rows = response['rows']
  row_format = '{:<20}' + '{:>20}' * 4
  print(row_format.format('Keys', 'Clicks', 'Impressions', 'CTR', 'Position'))
  for row in rows:
    keys = ''
    # Keys are returned only if one or more dimensions are requested.
    if 'keys' in row:
      keys = u','.join(row['keys']).encode('utf-8').decode()
    print(row_format.format(
        keys, row['clicks'], row['impressions'], row['ctr'], row['position']))

if __name__ == '__main__':
  main(sys.argv)