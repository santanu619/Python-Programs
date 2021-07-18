'''
@Author: Santanu Mohapatra
@Date: 11/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 14:00 PM
@Title:Program to find repeated element from a tuple.
'''
import logging
import loggerconfig

def repeatedTuple():
    '''
    Description: Function is used to find repeated element from a tuple.
    Parameters: Tuples.
    Return: None.
    ''' 
    try:
        mylist1 = []
        number = int(input("Enter the number of elements in a tuple:"))
        for index in range(0, number):
            elements = int(input("Elements:"))
            mylist1.append(elements)
        mytuple1 = tuple(mylist1)
        logging.info(mytuple1)
        for index in mytuple1:
            if mytuple1.count(index) > 1:
                logging.info(mytuple1[index])
    except Exception as e:
        logging.error(e)

if __name__=="__main__":
    repeatedTuple() 
    