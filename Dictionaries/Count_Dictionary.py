'''
@Author: Santanu Mohapatra
@Date: 09/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 19:10 PM
@Title: To count the value associated with a key in a dictionary.
'''
import logging

logging.basicConfig(filename='DataStructures.log',level=logging.DEBUG)

def countDictionary():
    '''
    Description: Function to count the value associated with a key in a dictionary.
    Parameters: String.
    Return: None.
    ''' 
    try:
        ratings = [{'id':1, 'rating':'good','movie':'EndGame'}, {'id':2, 'rating':'average','movie':'Chhalang'}, {'id':3, 'rating':'bad','movie':'Shaandar'}]
        print(sum(dictionary['id'] for dictionary in ratings))
        print(sum(dictionary['success'] for dictionary in ratings))
    except Exception as e:
        logging.critical(e)

if __name__=="__main__":
    countDictionary()