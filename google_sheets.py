import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import encryption
import json

class GoogleSheets:

    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file']

    credentials = 0
    client = 0

    def __init__(self, encrypted_client_secret_file): 
      dict = json.loads(encryption.decrypt(encrypted_client_secret_file))

      self.credentials = ServiceAccountCredentials.from_json_keyfile_dict(dict, self.scope)
      self.client = gspread.authorize(self.credentials)

    def get_sheet(self, sheet_name):
      return self.client.open(sheet_name)

