import gspread
from gspread.exceptions import SpreadsheetNotFound


class Gsheets:
    def __init__(self, sheet_name):
        self.sheet_name = sheet_name
        self.gs = gspread.service_account("utils/misc/google_sheets/config/service_account.json")
        self.wks = None

        

    
    def create_new_sheet(self):
        """Creating table templates"""

        sh = self.gs.create(self.sheet_name)
        sh.share(None, perm_type = 'anyone', role = 'writer')

        self.wks = sh.add_worksheet(title = "Пользователи", rows=10000, cols=10)
        old = sh.worksheet("Sheet1")
        sh.del_worksheet(old)


    def update_columns(self, line, username, fullname, role, company=None):
        # Opening
        sh = self.gs.open_by_url(self.get_url())
        self.wks = sh.worksheet("Пользователи")


        self.wks.update(f'A{line}', username)
        self.wks.update(f'B{line}', fullname)
        self.wks.update(f'C{line}', role)
        self.wks.update(f'D{line}', company)
    

    def get_url(self):
        try:
            self.gs.open(self.sheet_name)

        except SpreadsheetNotFound:
            self.create_new_sheet()

        finally:
            sh = self.gs.open(self.sheet_name)


        return "https://docs.google.com/spreadsheets/d/%s" % sh.id
    
