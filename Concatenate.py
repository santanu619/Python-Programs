'''
@Author: Santanu Mohapatra
@Date: 08/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 18:20 PM
@Title: To concatenate all elements in a list into a string and return it.
'''

def concatenatelist(list):
    '''
    Description: Function to concatenate all elements of list into strings.
    Parameters: List of numbers.
    Return: Result string.
    '''
    result= ''
    for element in list:
        result += str(element)
    return result

if __name__=="__main__":
    print(concatenatelist([8, 5, 6, 9]))