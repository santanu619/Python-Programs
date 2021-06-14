'''
@Author: Santanu Mohapatra
@Date: 09/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 08:20 AM
@Title: To create an array of 5 integers and display the array items.
'''

from array import *
import logging

logging.basicConfig(filename='array.log',level=logging.DEBUG)
def accessArray():
    '''
    Description: Function is used to access the array through it's indexes.
    Parameters: Array List.
    Return: None.
    '''
    try:
        array = []
        input_string = input("Enter a list element separated by space ")
        array  = input_string.split()
        logging.debug("Calculating sum of element of input list")
        logging.debug('Array:', array)
        logging.debug(array[1])
    except logging.exception as e:
        logging.critical(e)
if __name__=="__main__":
    accessArray()
