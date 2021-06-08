'''
@Author: Santanu Mohapatra
@Date: 08/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 18:00 PM
@Title: To create a histogram from the given list of integers.
'''

def histogram( items ):
    '''
    Description: Function to print the histogram from the given list.
    Parameters: List of numbers.
    Return: None.
    '''
    for number in items:
        pattern = ''
        times = number
        while( times > 0 ):
          pattern += '@'
          times = times - 1
        print(pattern)

if __name__=="__main__":
    histogram([3,8,5,4])