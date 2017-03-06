# U.S. Stock Market Activity Program (Stock Market Google Finance API)
# 2/21/17

import urllib.request
import googlefinance
import yahoo_finance
import json


def get_base_data_google(companies: list) -> list:
    '''
    Returns list of dicts specified exchange and companies with GoogleFinance.
    '''
    base_data = googlefinance.getQuotes(companies)
##    json_str = json.dumps(base_data[0])
##    json_data = json.loads(json_str)

    return base_data


def get_stock_yahoo(company: str) -> yahoo_finance.Share:
    '''
    Returns Yahoo finance Share class object.
    '''
    return yahoo_finance.Share(company)
