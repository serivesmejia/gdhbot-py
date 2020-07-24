import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import encryption

class GoogleSheets:

    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file']

    credentials = 0
    client = 0

    def __init__(self, client_secret_dict):

      self.credentials = ServiceAccountCredentials.from_json_keyfile_dict(client_secret_dict, self.scope)
      self.client = gspread.authorize(self.credentials)
      print("Logged in to google")

    def get_sheet(self, sheet_name):
      return self.client.open(sheet_name)

