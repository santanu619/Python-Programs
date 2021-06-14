'''
@Author: Santanu Mohapatra
@Date: 11/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 19:30 PM
@Title:Program to reverse a string.
'''
import logging
#import loggerconfig

def reverseString():
    '''
    Description: Function is used to reverse the string.
    Parameters: Strings.
    Return: None.
    '''
    try: 
        mystring = str(input("Enter the string:"))
        mystring = mystring[::-1]
        print(mystring)

    except Exception as e:
        logging.error(e)

if __name__=="__main__":
    reverseString()