'''
@Author: Santanu Mohapatra
@Date: 10/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 15:10 PM
@Title:Program to remove duplicates from the list.
'''
import logging
import loggerconfig

def copyList():
    '''
    Description: Function is used to copy the list.
    Parameters: List.
    Return: None.
    '''
    try:
        list1 = [1,2,3,4,5]
        print(str(list1))
        list2 = list1[:]
        print("LIST AFTER CLONNING:", list2)

    except Exception as e:
        logging.error(e)

if __name__=="__main__":
    copyList()