'''
@Author: Santanu Mohapatra
@Date: 10/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 18:10 PM
@Title:Program to find the list of words that are longer than n from a given list of words.
'''
import logging

def stringList():
    '''
    Description: Function is used to find the list of words that are longer than n from a given list of words.
    Parameters: List.
    Return: None.
    '''
    try:
        stringlist = []
        text = str.split("My name is Santanu Mohapatra")
        number = int(input("Enter the number:\n"))
        for element in text:
            if len(element) > number:
                stringlist.append(element)
        print(stringlist)
        
    except Exception as e:
        logging.error(e)

if __name__=="__main__":
    stringList()