'''
@Author: Santanu Mohapatra
@Date: 09/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 11:40 AM
@Title: To reverse the order of items in an array.
'''
from array import *
import logging

logging.basicConfig(filename='DataStructures.log',level=logging.DEBUG)

def reverseArray():
    '''
    Description: Function is used to print the array in reverse order.
    Parameters: Array List.
    Return: None.
    '''
    try:
        array = []
        input_string = input("Enter a list element separated by space ")
        array  = input_string.split()

        print("Original Array:\n")
        print(str(array))

        print("Reverse Array:\n")
        array.reverse()
        print(str(array))

    except Exception as e:
        logging.warning(e)

if __name__=="__main__":
    reverseArray()

