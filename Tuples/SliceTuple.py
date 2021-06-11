'''
@Author: Santanu Mohapatra
@Date: 11/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 15:30 PM
@Title:Program to slice a tuple.
'''
import logging
import loggerconfig

def sliceTuple():
    '''
    Description: 
    Parameters: Tuples.
    Return: None.
    ''' 
    try:
        list = []
        number = int(input("Enter the number of elements:"))
        for index in range(0, number):
            element = str(input())
            list.append(element)
        mytuple = tuple(list)
        logging.info(mytuple[::2])
    
    except Exception as e:
        logging.error(e)

if __name__=="__main__":
    sliceTuple()
