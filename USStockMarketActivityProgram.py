# U.S. Stock Market Activity Program (User Interface)
# 2/23/17

import stockmarket_csv_reader
import stockmarket_csv_writer
import stockmarket_class
import urllib.error
import time

def read_exchange() -> str:
    '''
    Reads and returns the user input exchange.
    '''
    exchange = input('Enter exchange symbol (NYSE, NASDAQ, or AMEX): ').strip().upper()

    return exchange


def read_api() -> str:
    '''
    Reads and returns the user input API.
    '''
    while True:
        api = input('Enter API (Google or Yahoo): ').strip().capitalize()

        if api == 'Google' or 'Yahoo':
            return api

        else:
            print('Invalid API')


def _split_symbols_list(companies: list) -> [list]:
    '''
    Returns a list of lists split 95 each for Google Finance limits.
    '''
    new_list = []

    if len(companies) % 95 != 0:
        num_of_lists = (len(companies) // 95) + 1
    else:
        num_of_lists = len(companies)

    for lst_num in range(num_of_lists):
        new_list.append(companies[:95])
        del companies[:95]

    return new_list


def user_interface() -> None:
    exchange = read_exchange()

    api = read_api()

    start_time = time.time()

    lst_companies = stockmarket_csv_reader.get_list_companies(exchange)

    csv_list = []

    if api == 'Google':
        for lst in _split_symbols_list(lst_companies):
            stocks = stockmarket_class.GoogleFinanceStocks(lst)

            for index in range(len(stocks.get_base_data())):
                print(stocks.get_stock_symbol(index), ':',
                      stocks.get_current_share_price(index))

                csv_list.append([stocks.get_stock_symbol(index),
                                 stocks.get_current_share_price(index)])

    elif api == 'Yahoo':
        count = 0
        
        for company in lst_companies:
            if count % 50 == 0 and count != 0:
                time.sleep(60)
                
            stock = stockmarket_class.YahooFinanceStocks(company)
            
            print(stock.get_stock_symbol(), ': ', stock.get_current_share_price())

            csv_list.append([stock.get_stock_symbol(), stock.get_current_share_price()])

##    for company in lst_companies:
##        try:
##            stock = stockmarket_class.GoogleFinanceStock(company)
##            print(stock.get_stock_symbol(), ': ', stock.get_current_share_price())
##            
##        except urllib.error.HTTPError as e:
##            print('HTTP Error: {}'.format(e.code))
##            if e.code == 503:
##                time.sleep(10)

    print('CSV File Path: ', end='')
    print(stockmarket_csv_writer.write_into_csv(csv_list, ['Symbol', 'Price per Share']))
    print()
    print('******************************')
    print('Total execution time:')
    print('--- %s seconds ---' % (time.time() - start_time))
    print('******************************')


if __name__ == '__main__':
    user_interface()
