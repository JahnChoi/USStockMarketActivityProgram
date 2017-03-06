# U.S. Stock Market Activity Program (Stock Exchange CSV Writer)
# 3/5/17

import csv
import os

def write_into_csv(csv_list: list, headers: list) -> str:
    '''
    Creates a CSV file from a string in the format of a CSV file and
    returns the path of the file.
    '''
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    with open('StockActivity.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        csv_writer.writerow(headers)

        for row in csv_list:
            csv_writer.writerow(row)

##        for row in _format_csv_string(string):
##            csv_writer.writerow(row)

    return dir_path + '\StockActivity.csv'


def _format_csv_string(string: str) -> list:
    '''
    Returns string of CSV as a list of rows.
    '''
    lst_split_by_row = string.split('\n')

    lst_for_csv_writing = []
    
    for row in range(len(lst_split_by_row)):
        lst_split_by_row[row] = lst_split_by_row[row].split(',')
        
        for item in range(len(lst_split_by_row[row])):
            lst_split_by_row[row][item] = lst_split_by_row[row][item].strip()
            
        lst_for_csv_writing.append([lst_split_by_row[row][0], lst_split_by_row[row][1]])

    return lst_for_csv_writing
