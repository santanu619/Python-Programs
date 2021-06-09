'''
@Author: Santanu Mohapatra
@Date: 08/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 16:40 PM
@Title: To generate a list and tuple
'''
num_list = input("Enter Comma-Separated Numbers: ")
list = num_list.split(",")
tuple = tuple(list)
'''
Print list from the comma-separated numbers.
'''
print('List : ',list)
'''
Print tuple from the comma-separated numbers.
'''
print('Tuple : ',tuple)
