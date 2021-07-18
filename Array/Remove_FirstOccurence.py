'''
@Author: Santanu Mohapatra
@Date: 09/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 12:25 PM
@Title: Program to remove the first occurence from the array.
'''
from array import *
import logging

logging.basicConfig(filename='DataStructures.log',level=logging.DEBUG)

def removefirstOccurence():
    '''
    Description: Function is used to remove the first occurence.
    Parameters: Array List.
    Return: None.
    '''
    try:
         array_first_occurence = []
         input_string = input("Enter a list element separated by space ")
         array_first_occurence  = input_string.split()

         print("Original Array:\n")
         print(str(array_first_occurence))
         
         print("Array Occurence:")
         array_first_occurence.remove('5')
         print(str(array_first_occurence))

    except Exception as e:
        logging.critical(e)

if __name__=="__main__":
    removefirstOccurence()