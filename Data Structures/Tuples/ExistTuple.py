'''
@Author: Santanu Mohapatra
@Date: 11/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 14:30 PM
@Title:Program to check whether an element exists within a tuple.
'''
import logging
import loggerconfig

def existTuple():
    '''
    Description: Function is used to check whether an element exists within a tuple.
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
        check = int(input("Enter the element to check:"))
        if check in mytuple:
            logging.info("The element is present.")
        else:
            logging.info("The element is not present.")
    
    except Exception as e:
        logging.error(e)

if __name__=="__main__":
    existTuple()