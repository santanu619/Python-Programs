'''
@Author: Santanu Mohapatra
@Date: 11/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 17:00 PM
@Title:Program to calculate the length and count the number of characters in a string.
'''
import logging
import loggerconfig

def countString():
    '''
    Description: Function is used to calculate the length and count the number of characters in a string.
    Parameters: Strings.
    Return: None.
    ''' 
    try:
        mystring = str(input("Enter the string:"))
        logging.info(len(mystring))
        stringcount = {}
        for index in mystring:
            if index in stringcount:
                stringcount[index] += 1
            else:
                stringcount[index] = 1
        logging.info((stringcount))

    except Exception as e:
        logging.error(e)

if __name__=="__main__":
    countString()