'''
@Author: Santanu Mohapatra
@Date: 08/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 16:00 PM
@Title: To print the first and last name in reverse order
'''

def user_firstname(fName):
    '''
    Description: This function is used to reverse the first name that has been given by the user.
    Parameters: firstName and the index value.
    Return: First Name in reverse order.
    '''
    firstName = ""
    for index in fName:
        firstName = index + firstName
    return firstName

def user_lastname(lName):
    '''
    Description: This function is used to reverse the last name that has been given by the user.
    Parameters: lastName and the index value.
    Return: Last Name in reverse order.
    '''
    lastName = ""
    for index in lName:
        lastName = index + lastName
    return lastName

if __name__ == "__main__":
    fName = input("Enter the First Name:\n")
    lName = input("Enter the Last Name:\n")
    print("Name is:",fName, lName)
    print("Name in reverse order:", user_lastname(lName), user_firstname(fName))