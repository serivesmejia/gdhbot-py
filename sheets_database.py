from google_sheets import GoogleSheets

class SheetsDatabase:

    gs = 0
    sheet = 0
    sheet_name = 0

    def __init__(self, sheet_name):
      self.gs = GoogleSheets("client_secret.json.fernet")
      self.sheet = self.gs.get_sheet(sheet_name)
      self.sheet_name = sheet_name

    def update_sheet(self):
      self.sheet = self.gs.get_sheet(self.sheet_name)

    def get_sheet(self):
      self.update_sheet()
      return self.sheet

    def get_worksheet_dict(self, index):
      return self.get_sheet().get_worksheet(index).get_all_values()

    