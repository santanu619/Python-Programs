'''
@Author: Santanu Mohapatra
@Date: 10/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 18:40 PM
@Title:Program that takes two lists and return true if it has atleast one common factor.
'''
import logging
import loggerconfig

def commondataList():
    '''
    Description: Function is used to take two lists and return true if it has atleast one common factor.
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

        for data in list1:
            if data in list2:
                print("The Data is present.")
                return True
            else:
                print("The data is not present.")
    except Exception as e:
        logging.error(e)

if __name__=="__main__":
    commondataList()


        
        
