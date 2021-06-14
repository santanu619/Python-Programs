'''
@Author: Santanu Mohapatra
@Date: 11/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 15:10 PM
@Title:Program to remove an item from a tuple.
'''
import logging
#import loggerconfig

def removeTuple():
    '''
    Description: 
    Parameters: Tuples.
    Return: None.
    ''' 
    try:
        list = []
        number = int(input("Enter the number of elements:"))
        for index in range(0, number):
            element = int(input())
            list.append(element)
        check = int(input("Enter the element to check:"))
        if check in list:
            list.remove(check)
            mytuple = tuple(list)
            print(mytuple)
        else:
            print("The element is not present.")
    
    except Exception as e:
        logging.error(e)

if __name__=="__main__":
    removeTuple()