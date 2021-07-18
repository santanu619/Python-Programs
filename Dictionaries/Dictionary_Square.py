'''
@Author: Santanu Mohapatra
@Date: 09/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 16:00 PM
@Title: To generate and print the dictionary that contains the number in the form of (x: x*x)
'''

import logging

logging.basicConfig(filename='DataStructures.log',level=logging.DEBUG)


def generateDictionary():
     '''
     Description: Function is used to generate and print the dictionary.
     Parameters: Dictionary.
     Return: None.
     '''
     try:
        number = int(input("Enter the number:\n"))
        dictionary = dict()

        for index in range(1,number+1):
            dictionary[index] = index*index

        print(dictionary)
     except Exception as e:
        logging.critical(e)

if __name__=="__main__":
    generateDictionary()

