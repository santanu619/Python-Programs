'''
@Author: Santanu Mohapatra
@Date: 11/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 11:30 AM
@Title:Program to create a tuple.
'''
import logging
import loggerconfig

def createTuple():
    '''
    Description: Function is used to create a tuple with same and different .
    Parameters: Tuples.
    Return: None.
    ''' 
    try:
        tuple1 = (1, 2, 3, 4)
        logging.info(tuple1)
        tuple2 = ("Santanu", True, 9.3, 9)
        logging.info(tuple2)
    except Exception as e:
        logging.error("Invalid Tuple", e)

if __name__=="__main__":
    createTuple()
