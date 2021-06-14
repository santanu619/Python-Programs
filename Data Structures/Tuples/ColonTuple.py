'''
@Author: Santanu Mohapatra
@Date: 11/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 12:50 PM
@Title:Program to create the colon of a tuple
'''
import logging
from copy import deepcopy
import loggerconfig

def colonTuple():
    '''
    Description: Function is used to create the colon of a tuple.
    Parameters: Tuples.
    Return: None.
    ''' 
    try:
        mycolon1 = ("s","a","n","t","a","n","u")
        mycolon2 = ()

        for data in mycolon1:
            mycolon2 = deepcopy(data)
            logging.info(mycolon2)

    except Exception as e:
        logging.error(e)

if __name__=="__main__":
    colonTuple()
        
