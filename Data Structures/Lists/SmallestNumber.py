'''
@Author: Santanu Mohapatra
@Date: 10/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 14:30 PM
@Title:Program to get the smallest number from the list.
'''
import logging
import loggerconfig

def smallest():
    '''
    Description: Function is used to find the smallest element from the list.
    Parameters: List.
    Return: None.
    '''
    try:
        list = []
        number = int(input("Enter the number of elements:\n"))
        for index in range(0, number):
            element = int(input())
            list.append(element)
        print(list)
        print("MINIMUM LIST:", min(list))

    except Exception as e:
        logging.error(e)

if __name__=="__main__":
    smallest()
