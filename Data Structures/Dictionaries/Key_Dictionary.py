'''
@Author: Santanu Mohapatra
@Date: 09/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 13:20 PM
@Title: To add a key to the dictionary
'''

import logging

logging.basicConfig(filename='DataStructures.log',level=logging.DEBUG)

def keyDictionary():
    '''
    Description: Function is used to add a key to a dictionary.
    Parameters: Dictionary.
    Return: None.
    '''
    try:
        dictionary = {0:10, 1:20, 3:15}
        print(dictionary)
        dictionary.update({2:30})
        print(dictionary)
        del dictionary[1]
        print(dictionary)
    except Exception as e:
        logging.critical(e)

if __name__=="__main__":
    keyDictionary()