'''
@Author: Santanu Mohapatra
@Date: 10/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 12:30 PM
@Title: Set functions.
'''

import logging
import loggerconfig

def setOperations():
    '''
    Description: Function is used to perform union, intersection, set difference, symmetric difference and clear the set.
    Parameters: Sets.
    Return: None.
    '''
    try:
        numberSets1 = set([0,1,2,3,4,5,6,7,8,9])
        numberSets2 = set([0,2,4,6,8,9])
        print(numberSets1)
        print(numberSets2)
        numberSets3 = set(numberSets1.union(numberSets2))
        print("UNION:\n")
        print(numberSets3)
        numberSets4 = set(numberSets1.intersection(numberSets2))
        print("INTERSECTION:\n")
        print(numberSets4)
        numberSets5 = set(numberSets1.difference(numberSets2))
        print("SET DIFFERENCE:\n")
        print(numberSets5)
        numberSets6 = set(numberSets1.symmetric_difference(numberSets2))
        print("SYMMETRIC DIFFERENCE:\n")
        print(numberSets6)
        frozensets = frozenset(['a','b','c','d'])
        print(frozensets)
        print("MAXIMUM in Set 1:\n")
        numberSets2 = set.clear()
        print(numberSets2)
    except Exception as e:
        logging.error(e)

if __name__=="__main__":
    setOperations()