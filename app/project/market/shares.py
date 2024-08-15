from flask import Blueprint
import openpyxl


shares = Blueprint('market', __name__, url_prefix='/market')

@shares.route('/shares')
def live():
    shares = read_excel_file_and_process_shares();
    return 'market_test', 200


class Share:
    def __init__(self, date, ticker, money):
        self._date = None
        self._ticker = None
        self._money = None

        self.date = date
        self.ticker = ticker
        self.money = money
            
    # Date property
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    # Ticker property
    @property
    def ticker(self):
        return self._ticker

    @ticker.setter
    def ticker(self, value):
        self._ticker = value

    # Money property
    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        self._money = value       
        
        
def read_excel_file_and_process_shares():
    wb = openpyxl.load_workbook(r"C:\Users\macy\VisualStudio\app\market.xlsx")
    sheet = wb["shares"]
    shares_list = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        date, ticker, money = row
        share = Share(date=date, ticker=ticker, money=money)
        shares_list.append(share)
    return shares_list