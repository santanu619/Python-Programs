'''
@Author: Santanu Mohapatra
@Date: 10/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 17:20 PM
@Title:Program to get the difference between two lists.
'''
import logging
import loggerconfig

def differenceList():
    '''
    Description: Function is used to get the difference between two list.
    Parameters: List.
    Return: None.
    '''
    try:
        list1 = []
        list2 = []
        number1 = int(input("Enter the number of elements in list 1:"))
        number2 = int(input("Enter the number of elements in list 2:"))
        for index in range(0,number1):
            element1 = int(input())
            list1.append(element1)
        print(str(list1))
        for j in range(0, number2):
            element2 = int(input())
            list2.append(element2)
        print(str(list2))
        differList = []
        for data in list1:
            if not data in list2:
                differList.append(data)
        print(str(differList))
    except Exception as e:
        logging.error(e)

if __name__=="__main__":
    differenceList()