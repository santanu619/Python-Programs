'''
@Author: Santanu Mohapatra
@Date: 09/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 08:20 AM
@Title: To create an array of 5 integers and display the array items.
'''

from array import *

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
        print("Calculating sum of element of input list")
        print(array)
        print(array[1])
    except ValueError as e:
        print(e)
if __name__=="__main__":
    accessArray()


