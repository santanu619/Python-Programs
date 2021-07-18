'''
@Author: Santanu Mohapatra
@Date: 10/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 14:10 PM
@Title:Program to find the sum and multiplication of a list.
'''
import logging
import loggerconfig


def sum_multiply():
    '''
    Description: Function is used to find the sum and multiplication of the list.
    Parameters: List.
    Return: None.
    '''
    try:
        list = []
        number = int(input("Enter the number of elements:\n"))
        for index in range(0, number):
            element = int(input())
            list.append(element)
        print("LIST:\n")
        print(list)
        sums = 0
        for data_sum in list:
            sums += data_sum
        print("SUM OF LIST:", sums)
        multiplication = 1
        for data_multiply in list:
            multiplication *= data_multiply
        print("MULTIPLICATION OF LIST:", multiplication)
    except Exception as e:
        logging.error(e)

if __name__=="__main__":
    sum_multiply()