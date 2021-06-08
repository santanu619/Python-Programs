'''
@Author: Santanu Mohapatra
@Date: 08/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 17:05 PM
@Title: To print the calendar.
'''

import calendar

def calendar_monthyear():
    '''
    Description: Functions to print the year and month.
    Parameters: Year and month.
    Return: None.
    '''
    year = int(input("Input the year : "))
    month = int(input("Input the month : "))
    print(calendar.month(year, month))

if __name__=="__main__":
    calendar_monthyear()