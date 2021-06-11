'''
@Author: Santanu Mohapatra
@Date: 10/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 20:10 PM
@Title:Program to find common items between two lists.
'''
import logging
import loggerconfig

def commonitemList():
    '''
    Description: Function is used to find common items between two lists.
    Parameters: List.
    Return: None.
    '''
    try:
        list1 = []
        list2 = []

        number = int(input("Enter the number of elements in list 1 and list 2:"))
        
        #LIST 1
        print("Enter the elements for list 1:\n")
        for index in range(0, number):
            element1 = int(input())
            list1.append(element1)

        #LIST 2
        print("Enter the elements for list 2:\n")
        for index in range(0, number):
            element2 = int(input())
            list2.append(element2)

        print("List 1:\n")
        print(list1)

        print("List 2:\n")
        print(list2)

        commonlist = []
        for data in list1:
            if data in list2:
                commonlist.append(data)

        print("COMMON LIST:", commonlist)
    
    except Exception as e:
        logging.error(e)

if __name__=="__main__":
    commonitemList()