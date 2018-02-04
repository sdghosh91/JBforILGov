from __future__ import print_function
import httplib2
import os
import pandas as pd
import csv

import os
import pandas as pd
import zipfile
from zipfile import ZipFile
import re
import time

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
# code for extracting zip file -------------------------------------------------
    # set variables
    exportTime1 = "6PM"
    exportTime2 = "8PM"
    exportType1 = "tpexport"
    exportType2 = "EventParticipantReport"
    year, month, day = time.strftime("%Y,%m,%d").split(',')
    exportDate = year+month+day
    fileName1 = exportTime1 + exportType1 + exportDate # call time 6PM
    fileName2 = exportTime2 + exportType1 + exportDate # call time 8PM
    fileName3 = exportType2 # confirm

    path = r'C:\Users\Natalie Tham\Downloads'

    # select .zip file based on exportTime, exportDate, exportType
    for i in os.listdir(path): # looks in path folder
        # if file starts with fileName + ends in .zip + is in path
        if os.path.isfile(os.path.join(path,i)) and i.endswith('.zip') and i.startswith(fileName2):
            j = os.path.join(path,i)
            with zipfile.ZipFile(j,"r") as zip_ref:
                zip_ref.extractall(path)
                zip_ref.close()
                #os.remove(j) remove zip
        if os.path.isfile(os.path.join(path,i)) and i.endswith('.zip') and i.startswith(fileName3):
            j = os.path.join(path,i)
            with zipfile.ZipFile(j,"r") as zip_ref:
                zip_ref.extractall(path)
                zip_ref.close()
                #os.remove(j) remove zip

    for k in os.listdir(path):
        if os.path.isfile(os.path.join(path,k)) and k.endswith('.txt') and k.startswith(fileName2):
            m = os.path.join(path,k) # this is the extracted file path
        if os.path.isfile(os.path.join(path,k)) and k.endswith('.xls') and k.startswith(fileName3):
            n = os.path.join(path,k) # this is the extracted file path
# ------------------------------------------------------------------------------

# import file into a tempList : duplicate code for each new file ---------------
    tempList2 = []  # test should be initialized in the function body
    with open(os.path.abspath(m), 'rt') as f:
        reader = csv.reader(f, delimiter =  '\t')
        for row in reader:
            tempList2.append(row)
        df = 'tempList2' # call time 8PM

    tempList3 = []  # test should be initialized in the function body
    with open(os.path.abspath(n), 'rt') as f:
        reader = csv.reader(f, delimiter =  '\t')
        for row in reader:
            tempList3.append(row)
        df = 'tempList3' # confirm
# ------------------------------------------------------------------------------
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
    # specify spreadsheetID(s), sheet name(s)
    spreadsheetId1 = '19HRYvamCexyhnOzwCj-p-aCdHxwmeHi-g6L9o8K4vbc' # call time
    spreadsheetId2 = '1DCrWd3PLe4NQsPy7b7X8sFxLP_rN8qSDruRMP36fOYE' # confirm
    rangeName1 = 'test6PM'
    rangeName2 = 'test8PM'
    rangeName3 = 'testrawdata'

    """ **not sure what this does**
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])
    """
# clear current data from sheet--------------
    batch_clear_values_request_body = {
    # A list of updates to apply to the spreadsheet.
    # Requests will be applied in the order they are specified.
    # If any request is not valid, no requests will be applied.

    # specify which sheets to clear
    'ranges': ['test8PM'],
    }

    request = service.spreadsheets().values().batchClear(spreadsheetId=spreadsheetId1, body=batch_clear_values_request_body)
    response = request.execute()

    # clear confirm report
    batch_clear_values_request_body = {
    'ranges': ['testrawdata'],
    }

    request = service.spreadsheets().values().batchClear(spreadsheetId=spreadsheetId2, body=batch_clear_values_request_body)
    response = request.execute()
# -----------------------------------------

# add data from tempList : duplicate code for each new file --------------
    values2 = {'values': tempList2}
    result = service.spreadsheets().values().append(
        spreadsheetId=spreadsheetId1, range=rangeName2,
        valueInputOption='RAW',
        body=values2).execute()

    values3 = {'values': tempList3}
    result = service.spreadsheets().values().append(
        spreadsheetId=spreadsheetId2, range=rangeName3,
        valueInputOption='RAW',
        body=values3).execute()
# -------------------------------------------------------------------------

if __name__ == '__main__':
    main()
