'''
@Author: Santanu Mohapatra
@Date: 09/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 13:50 PM
@Title: To iterate over a dictionary using for loop
'''
import logging

logging.basicConfig(filename='DataStructures.log',level=logging.DEBUG)

def iterateDictionary():
    '''
    Description: Function is used to iterate through a dictionary using for loops.
    Parameters: Dictionary.
    Return: None.
    '''
    try:
        name_dictionary = {'a':'Santanu', 'b':'Sasmita', 'c': 'Laxmi Prasad'}
        for key, value in name_dictionary.items():
            print(key, value)
    except Exception as e:
        logging.critical(e)

if __name__=="__main__":
    iterateDictionary()