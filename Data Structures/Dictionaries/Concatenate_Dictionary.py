'''
@Author: Santanu Mohapatra
@Date: 09/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 14:20 PM
@Title: To concatenate dictionaries
'''
import logging

logging.basicConfig(filename='DataStructures.log',level=logging.DEBUG)

def concatenateDictionary():
    '''
    Description: Function is used to concatenate dictionaries.
    Parameters: Dictionary.
    Return: None.
    '''
    try:
        dictionary1={1:10, 2:20}
        dictionary2={3:30, 4:40}
        dictionary3={5:50,6:60}
        dictionary4 = {}
        for index in (dictionary1, dictionary2, dictionary3): 
            dictionary4.update(index)
        print(dictionary4)
    except Exception as e:
        logging.critical(e)

if __name__=="__main__":
    concatenateDictionary()