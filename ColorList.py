'''
@Author: Santanu Mohapatra
@Date: 08/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 16:50 PM
@Title: To print the first and last colour from the list.
'''
def first_last_colour():
    '''
    Description: Functions is used to print the first and last colour from the list.
    Parameters: List of colours.
    Return: None.
    '''
    try:
        color_list = ["Red","Green","White" ,"Black"]
        print( "%s %s"%(color_list[0],color_list[-1]))
    except ValueError as e:
        print(e)
if __name__=="__main__":
    first_last_colour()