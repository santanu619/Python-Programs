'''
@Author: Santanu Mohapatra
@Date: 09/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 16:40 PM
@Title: To print unique values from the dictionary.
'''
import logging

logging.basicConfig(filename='DataStructures.log',level=logging.DEBUG)

def uniqueDictionary():
    '''
    Description: Function is used to find unique values in a dictionary.
    Parameters: Dictionary.
    Return: None.
    ''' 
    try:
        dictionary = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
        print("Original List: ", dictionary)
        uniqueValue = set( value for dic in dictionary for value in dic.values())
        print("Unique Values: ",uniqueValue)    
    except Exception as e:
        logging.critical(e)

if __name__=="__main__":
    uniqueDictionary()