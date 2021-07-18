'''
@Author: Santanu Mohapatra
@Date: 10/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 19:30 PM
@Title:Program to append a list from the second list.
'''
import logging

def appendList():
    '''
    Description: Function is used to append a list to the second list.
    Parameters: List.
    Return: None.
    '''
    try:
        list1 = []
        number = int(input("Enter the number of elements in list 1:"))
        
        #LIST 1
        print("Enter the elements for list 1:\n")
        for index in range(0, number):
            element = int(input())
            list1.append(element)
        print(list1)

        list2 = []
        list2.append(list1)
        print("LIST 2:", list2)

    except Exception as e:
        logging.error(e)

if __name__=="__main__":
    appendList()

        

