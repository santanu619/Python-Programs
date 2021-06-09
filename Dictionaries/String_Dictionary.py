'''
@Author: Santanu Mohapatra
@Date: 09/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 17:30 PM
@Title: To print unique values from the dictionary.
'''
import logging

logging.basicConfig(filename='DataStructures.log',level=logging.DEBUG)

def uniqueDictionary():
    '''
    Description: Function is used to create a dictionary from the string.
    Parameters: String.
    Return: None.
    ''' 
    try:
        string = 'SantanuMohapatra'
        dictionary = {}
        for key in string:
            dictionary[key] = dictionary.get(key, 0) + 1
        print(dictionary)
    except Exception as e:
        logging.critical(e)

if __name__=="__main__":
    uniqueDictionary()
  