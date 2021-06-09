'''
@Author: Santanu Mohapatra
@Date: 08/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 18:40 PM
@Title: To print out a set containing all the colors from color_list_1 which are not present in color_list_2
'''
try:
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])

    print(color_list_1.difference(color_list_2))

except ValueError as e:
    print(e)