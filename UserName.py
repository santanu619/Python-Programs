'''
@Author: Santanu Mohapatra
@Date: 01/06/2021
@Title: To replace UserName with input in Hello Statement
'''

try:
    username=input("Enter Your UserName:")
except ValueError:
    print("Wrong. Please Enter the correct UserName....")
if len(username) < 3:
    print("Username should have minimum of 3 characters")
else:
    print("Hello", username, "How are you?")
