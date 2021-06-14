'''
@Author: Santanu Mohapatra
@Date: 11/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 16:10 PM
@Title:Program to reverse a tuple.
'''
import logging
import loggerconfig

def sliceTuple():
    '''
    Description: Function is used to reverse a tuple.
    Parameters: Tuples.
    Return: None.
    ''' 
    try:
        list = []
        number = int(input("Enter the number of elements:"))
        for index in range(0, number):
            element = int(input())
            list.append(element)
        mytuple = tuple(list)
        logging.info("ORIGINAL TUPLE:", mytuple)
        logging.info("REVERSED TUPLE: ", mytuple[::-1])
    
    except Exception as e:
        logging.error(e)

if __name__=="__main__":
    sliceTuple()