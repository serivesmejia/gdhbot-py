from google_sheets import GoogleSheets
import os
import json
import encryption
from df2gspread import df2gspread as d2g
import pandas as pd

def from_file(sheet_name, filename, decrypt_key):
    str = open(filename,"r").read()

    str = encryption.decrypt_str(str, decrypt_key)

    return SheetsDatabase(sheet_name, str)

def from_file(sheet_name, filename):
    str = open(filename,"r").read()

    return SheetsDatabase(sheet_name, str)

class SheetsDatabase:
    gs = 0
    sheet = 0
    sheet_name = 0
    sheet_key = 0

    last_dataframes = dict()

    def __init__(self, sheet_name, sheet_key, client_secret_json_str):
      self.gs = GoogleSheets(json.loads(client_secret_json_str))
      self.sheet_key = sheet_key

      self.sheet_name = sheet_name
      self.sheet = self.gs.get_sheet(self.sheet_name)

    def update_sheet(self):
      self.sheet = self.gs.get_sheet(self.sheet_name)

    def get_sheet(self, updatesheet):
      if(updatesheet): self.update_sheet()
      return self.sheet

    def get_worksheet_dict(self, worksheet_name, updatesheet):
      return self.get_sheet(updatesheet).worksheet(worksheet_name).get_all_values()

    def get_worksheet_dataframe(self, worksheet_name, updatesheet):
      data = self.get_worksheet_dict(worksheet_name, updatesheet)
      self.last_dataframes[worksheet_name] = pd.DataFrame(data)
      return self.last_dataframes[worksheet_name]

    def get_last_worksheet_dataframe(self, worksheet_name):
      return self.last_dataframes[worksheet_name]

    def push_dataframe(self, worksheet_name, dataframe):
      d2g.upload(dataframe, self.sheet_key, worksheet_name, credentials=self.gs.credentials, row_names=False, col_names=False)

    def change_value_push(self, worksheet_name, x, y, value, update_last_dataframe):
      self.change_value(worksheet_name, x, y, value, update_last_dataframe)
      self.push_last_dataframe(worksheet_name)

    def change_value(self, worksheet_name, x, y, value, update_last_dataframe):
      if(update_last_dataframe): self.get_worksheet_dataframe(worksheet_name, update_last_dataframe)
      self.last_dataframes[worksheet_name].at[x,y] = value
    
    def push_last_dataframe(self, worksheet_name):
      self.push_dataframe(worksheet_name, self.last_dataframes[worksheet_name])