'''
@Author: Santanu Mohapatra
@Date: 09/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 12:50 PM
@Title: To reverse the order of items in an array.
'''
import logging
import operator

logging.basicConfig(filename='DataStructures.log',level=logging.DEBUG)

def sortDictionary():
    '''
    Description: Function is used to sort the dictionary.
    Parameters: Dictionary.
    Return: None.
    '''
    try:
        dictionary = {1:2, 2:0, 3:5, 4:6, 5:9}
        print("Original Dictionary:", dictionary)
        ascending_sorting = sorted(dictionary.items(), key=operator.itemgetter(1))
        print('Dictionary in ascending order by value : ',ascending_sorting)
        descending_sorting = dict( sorted(dictionary.items(), key=operator.itemgetter(1),reverse=True))
        print('Dictionary in descending order by value : ',descending_sorting)

    except Exception as e:
        logging.critical(e)

if __name__=="__main__":
    sortDictionary()