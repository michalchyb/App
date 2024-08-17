from datetime import datetime
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
        self._date = self.date_validator(value)

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
        self._money = self.validate_money(value)      
    
    @staticmethod
    def date_validator(value):
        try:
            return datetime.strptime(str(value), '%d.%m.%Y').date()
        except ValueError:
            raise ValueError(f"Invalid date format for date: {value}. Expected format: YYYY-MM-DD.")

    @staticmethod
    def validate_money(money_str):
        try:
            money_value = float(money_str)
            if money_value <= 0:
                raise ValueError(f"Money value must be positive. Got: {money_value}")
            return money_value
        except ValueError:
            raise ValueError(f"Invalid money value: {money_str}. It must be a positive number.")
     
    def __repr__(self):
        return f"Share(date={self.date}, ticker='{self.ticker}', money={self.money})"

def read_excel_file_and_process_shares():
    file_path = r"C:\Users\macy\VisualStudio\app\market.xlsx"
    wb = load_workbook(file_path)
    sheet = wb["shares"]
    return process_sheet(sheet)


def load_workbook(file_path) -> openpyxl.Workbook:
    return openpyxl.load_workbook(file_path)

def process_sheet(sheet) : 
    shares_list = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        share = create_share_from_row(row)
        shares_list.append(share)
    return shares_list

def create_share_from_row(row) -> Share:
    date, ticker, money = row
    return Share(date=date, ticker=ticker, money=money)
