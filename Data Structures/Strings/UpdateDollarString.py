'''
@Author: Santanu Mohapatra
@Date: 11/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 17:00 PM
@Title:Program to update the string with $ if a same character altered twice.
'''
import logging
#import loggerconfig

def replacedollarString():
    '''
    Description: Function is used to update the string with $ if a same character altered twice.
    Parameters: Strings.
    Return: None.
    ''' 
    try:
        mystring = str(input("Enter the string:"))
        print(mystring)
        character = mystring[0]
        mystring = mystring.replace(character, '$')
        mystring = character + mystring[1:]
        print(mystring)
            
    except Exception as e:
        logging.error(e)

if __name__=="__main__":
    replacedollarString()