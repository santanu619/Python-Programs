'''
@Author: Santanu Mohapatra
@Date: 08/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 17:40 PM
@Title: To check whether a specified value is contained in a group of values.
'''

def check_groupMember(data_list, number):
    '''
    Description: Functions to check if a value exists in that list or not.
    Parameters: List and the given number.
    Return: Return true if number exists or false.
    '''
    try:
        for value in data_list:
            if number == value:
                return True
        return False
    except ValueError as e:
        print(e)
if __name__=="__main__":
    print(check_groupMember([1, 5, 8, 3], 3))
    print(check_groupMember([1, 5, 8, 3], -1))