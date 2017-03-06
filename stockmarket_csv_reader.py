# U.S. Stock Market Activity Program (Stock Exchange CSV Reader)
# 3/4/17

import csv

EXCHANGE_DICT = {'AMEX': 'C:\\Users\\JahnC\\Desktop\\Stock Market API\\Stock Exchange CSVs\\AMEXcompanylist.csv',
                 'NASDAQ': 'C:\\Users\\JahnC\\Desktop\\Stock Market API\\Stock Exchange CSVs\\NASDAQcompanylist.csv',
                 'NYSE': 'C:\\Users\\JahnC\\Desktop\\Stock Market API\\Stock Exchange CSVs\\NYSEcompanylist.csv'}

def _clean_up_list(companies: list) -> list:
    '''
    Returns the same list of companies, except with all
    extraneous symbols and repeated stocks deleted.
    '''
    new_list = []
    
    for company in companies:
        if '^' in company:
            new_list.append(company[:company.index('^')].strip())

##        elif '.' in company:
##            new_list.append(company[:company.index('.')])

        elif company == 'Symbol':
            pass

        else:
            new_list.append(company.strip())

    new_list = list(set(new_list))

    new_list.sort()

    return new_list


def get_list_companies(exchange: str) -> list:
    '''
    Returns a list of all company symbols in specified exchange.
    '''
    result = []
    
    with open(EXCHANGE_DICT[exchange], 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        
        for row in csv_reader:
            if len(row) != 0:
                result.append(row[0])

    result = _clean_up_list(result)

    return result
