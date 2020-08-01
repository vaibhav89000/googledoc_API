import gspread
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client = gspread.authorize(creds)

sheet = client.open('project').sheet1
spreadsheet_id=''
values = sheet.get_all_records()
print(values)
service = build('sheets', 'v4', credentials=creds)
# result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
result = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
rows = result.get('values', [])
print('{0} rows retrieved.'.format(len(rows)))