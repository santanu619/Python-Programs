'''
@Author: Santanu Mohapatra
@Date: 09/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 18:10 PM
@Title: To print a dictionary in table format.
'''
import logging

logging.basicConfig(filename='DataStructures.log',level=logging.DEBUG)

def tableDictionary():
    '''
    Description: Function to print a dictionary in a table format.
    Parameters: String.
    Return: None.
    ''' 
    try:
        dictionary = {'Fruits': ['Watermelon','Pineapple','Kiwi','Strawberry'], 'Vegetables':['Cauliflower','Beans','Carrot'], 'Flowers':['Lotus','Jasmine','Rose']}
        for index in zip(*([key] + (value) for key, value in sorted(dictionary.items()))):
            print(*index) 

    except Exception as e:
        logging.critical(e)
    
if __name__=="__main__":
    tableDictionary()