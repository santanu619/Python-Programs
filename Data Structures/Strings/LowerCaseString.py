'''
@Author: Santanu Mohapatra
@Date: 11/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 19:40 PM
@Title:Program to lowercase first n characters of a string.
'''
import logging
import loggerconfig

def lowercaseString():
    '''
    Description: Function is used to lowercase first n characters of a string .
    Parameters: Strings.
    Return: None.
    '''
    try: 
        mystring = str(input("Enter the string:"))
        number = int(input("Enter the number:"))
        logging.info(mystring)
        logging.info((mystring[:number].lower())+ mystring[number:])

    except Exception as e:
        logging.error(e)

if __name__=="__main__":
    lowercaseString()