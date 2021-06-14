'''
@Author: Santanu Mohapatra
@Date: 10/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 14:50 PM
@Title:Program to remove duplicates from the list.
'''
import logging
import loggerconfig

def removeDuplicates():
    '''
    Description: Function is used to remove duplicates from the list.
    Parameters: List.
    Return: None.
    '''
    try:
        list = [1,2,3,4,5,5,5,6,4,3,2,2,2,1]
        print(list)
        duplicates = []
        for data in list:
            if data not in duplicates:
                duplicates.append(data)
        print(str(duplicates))
    
    except Exception as e:
        logging.error(e)

if __name__=="__main__":
    removeDuplicates()