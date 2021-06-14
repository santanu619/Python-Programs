'''
@Author: Santanu Mohapatra
@Date: 10/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 13:10 PM
@Title: Maximum element and minimum element in a set.
'''

import logging
#import loggerconfig

def maximum_minimum():
    '''
    Description: Function is used to find the maximum and minimum element in the set.
    Parameters: Sets.
    Return: None.
    '''
    try:
        mySet = set()
        
        number = int(input("Enter the number of elements in the set:\n"))
        for index in range(0, number):
            mySet.add(index)
        
        print(mySet)
        
        minimum = 99
        for data_min in mySet:
            if int(data_min) < minimum:
                minimum = data_min
        print("Minimum value is:", minimum)
        
        maximum = 0
        for data_max in mySet:
            if data_max > maximum:
                maximum = data_max
        print("Maximum value is:", maximum)
        '''
        print("MINIMUM:\n")
        print(min(mySet))
        print("MAXIMUM:\n")
        print(max(mySet))
        '''
    except Exception as e:
        logging.error(e)

if __name__=="__main__":
    maximum_minimum()