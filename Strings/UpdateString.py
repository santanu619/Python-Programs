'''
@Author: Santanu Mohapatra
@Date: 11/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 17:50 PM
@Title:Program to update the string with 'ing' or 'ly'.
'''
import logging
#import loggerconfig

def updateString():
    '''
    Description: Function is used to update the string with 'ing' or 'ly'.
    Parameters: Strings.
    Return: None.
    ''' 
    try:
        mystring = str(input("Enter the string:"))
        print(mystring)
        if len(mystring) > 2:
            if mystring[-3:] == 'ing':
                mystring += 'ly'
                print(mystring)
            else:
                mystring += 'ing'
                print(mystring)
                
    except Exception as e:
        logging.error(e)

if __name__=="__main__":
    updateString()        