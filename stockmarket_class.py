# U.S. Stock Market Activity Program (Stock Exchange & Company Class)
# 3/4/17

import stockmarket_api

class StockExchange:
    def __init__(self):
        pass

class StockCompany:
    def __init__(self):
        pass

class GoogleFinanceStocks:                  # Google finance is real-time
    def __init__(self, companies: list):
        self._companies = companies
        self._base_data = stockmarket_api.get_base_data_google(companies)


    def get_base_data(self) -> list:
        '''
        Returns the list base data retrieves from Google Finance.
        '''
        return self._base_data


    def get_stock_symbol(self, index: int) -> str:
        '''
        Returns the stock symbol for the company.
        '''
        return self._base_data[index]['StockSymbol']


    def get_current_share_price(self, index: int) -> float:
        '''
        Returns the current price per share as a float.
        '''
        return self._base_data[index]['LastTradeWithCurrency']


    def get_last_trade_time(self, index: int) -> str:
        '''
        Returns the last trade time of the stock.
        '''
        return self._base_data[index]['LastTradeDateTimeLong']


class YahooFinanceStocks:                   # Yahoo finance is delayed by 15 minutes
    def __init__(self, company: str):
        self._company = company
        self._stock = stockmarket_api.get_stock_yahoo(company)


    def get_stock_symbol(self) -> str:
        '''
        Returns stock symbol for the company.
        '''
        return self._company
    

    def get_company_name(self) -> str:
        '''
        Returns full company name.
        '''
        return self._stock.get_name()


    def get_current_share_price(self) -> float:
        '''
        Returns the current price per share as an integer.
        '''
        return float(self._stock.get_price())


    def get_last_trade_time(self) -> str:
        '''
        Returns the last trade time of the stock.
        '''
        return self._stock.get_trade_datetime()
