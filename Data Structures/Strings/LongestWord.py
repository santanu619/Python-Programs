'''
@Author: Santanu Mohapatra
@Date: 11/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 18:30 PM
@Title:Program that takes a list of words and returns the length of the longest one.
'''
import logging
#import loggerconfig

def longestWord():
    '''
    Description: Function is used to take a list of words and returns the length of the longest one.
    Parameters: Strings.
    Return: None.
    '''
    try: 
        mylist = []
        number = int(input("Enter the number of words:"))
        for index in range(0, number):
            words = str(input("WORD:"))
            mylist.append(words)
        print(mylist)
        longest = len(mylist[0])
        for data in mylist:
            if len(data) > longest:
                longest = mylist[data]
        print(longest)
    except Exception as e:
        logging.error(e)

if __name__=="__main__":
    longestWord()
