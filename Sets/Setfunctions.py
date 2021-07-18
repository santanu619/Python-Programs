'''
@Author: Santanu Mohapatra
@Date: 10/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 11:15 AM
@Title: Set functions.
'''
import logging
import loggerconfig
def functionsSet():
    '''
    Description: Function is used to create a set.
    Parameters: Sets.
    Return: None.
    ''' 
    try:
        print("Define the empty set function:")
        myset = set()
        print(myset)
        number = int(input("Enter the number of elements you want to add in the set:\n"))
        for index in range(0, number):
            myset.add(index)
        print("The Elements are:\n", myset)

        #Iterating over sets
        sampleset = set(['s','a','n','t','a','n','u'])
        for value in sampleset:
            print(value)
        
        #Remove Item from the set
        myset.remove(2)
        print(myset)

        #Another set
        character_set = set(['a','p','p','l','e'])
        if 'a' in character_set:
            character_set.remove('a')
            print(character_set)
        else:
            print("Element not found!")

    except Exception as e:
        logging.error(e)

if __name__=="__main__":
    functionsSet()

