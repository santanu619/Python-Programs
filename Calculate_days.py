'''
@Author: Santanu Mohapatra
@Date: 08/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 17:20 PM
@Title: To calculate number of days between two dates.
'''

from datetime import date

def calculate_days():
    '''
    Description: Functions to calculate number of days between two dates.
    Parameters: First date and last date.
    Return: None.
    '''
    first_date = date(2014, 7, 2)
    last_date = date(2014, 7, 11)
    delta = last_date - first_date
    print(delta.days)

if __name__=="__main__":
    calculate_days()