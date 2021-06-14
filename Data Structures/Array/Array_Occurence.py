'''
@Author: Santanu Mohapatra
@Date: 09/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 12:10 PM
@Title: Program to get the number of occurences of a sprcified elements in an array.
'''
from array import *
import logging

logging.basicConfig(filename='DataStructures.log',level=logging.DEBUG)

def occurenceArray():
    '''
    Description: Function is used to get the number of occurences of a specified element in an array.
    Parameters: Array List.
    Return: None.
    '''
    try:
        array_occurence = []
        input_string = input("Enter a list element separated by space ")
        array_occurence  = input_string.split()

        print("Original Array:\n")
        print(str(array_occurence))

        print("Array Occurence:")
        print(str(array_occurence.count('5')))

    except Exception as e:
        logging.critical(e)

if __name__=="__main__":
    occurenceArray()