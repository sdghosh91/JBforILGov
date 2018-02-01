from __future__ import print_function
import httplib2
import os
import pygsheets
import pandas as pd
import csv

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Quickstart'

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
# read csv into list named tempList ------------
    tempList1 = []  # test should be initialized in the function body
    with open(r'C:\Users\Natalie Tham\Downloads\targetexporttxt20180129-5880626869.csv', 'rt') as f:
        reader = csv.reader(f)
        for row in reader:
                tempList1.append(row)

    tempList2 = []  # test should be initialized in the function body
    with open(r'C:\Users\Natalie Tham\Downloads\targetexporttxt20180129-5880626869.csv', 'rt') as f:
        reader = csv.reader(f)
        for row in reader:
                tempList2.append(row)
# ----------------------------------------------
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '19HRYvamCexyhnOzwCj-p-aCdHxwmeHi-g6L9o8K4vbc'
    rangeName1 = 'test6PM'
    rangeName2 = 'test8PM'

    """ **not sure what this does**
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])
    """
# clear current data from sheet-----
    batch_clear_values_request_body = {
    # A list of updates to apply to the spreadsheet.
    # Requests will be applied in the order they are specified.
    # If any request is not valid, no requests will be applied.
    'ranges': ['test6PM', 'test8PM'],
    }

    request = service.spreadsheets().values().batchClear(spreadsheetId=spreadsheetId, body=batch_clear_values_request_body)
    response = request.execute()
# ----------------------------------

# add data from tempList -----------
    values1 = {'values': tempList1}
    result = service.spreadsheets().values().append(
        spreadsheetId=spreadsheetId, range=rangeName1,
        valueInputOption='RAW',
        body=values1).execute()

    values2 = {'values': tempList2}
    result = service.spreadsheets().values().append(
        spreadsheetId=spreadsheetId, range=rangeName2,
        valueInputOption='RAW',
        body=values2).execute()
# ----------------------------------

if __name__ == '__main__':
    main()
