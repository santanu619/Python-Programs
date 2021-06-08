'''
@Author: Santanu Mohapatra
@Date: 01/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 12:00 PM
@Title: To print the 2 Dimensional Array using Function
'''
try:
    rows = int(input("Enter the number of rows "))
    columns = int(input("Enter the number of columns "))
except ValueError: 
    print("Enter correct input")

#To create function to print 2D Array
    def Array():
        try:
            arraycreation=[]
            for i in range(rows):
                value = []
                for j in range(columns):
                    element = int(input("Enter the element"))
                    value.append(element)
                arraycreation.append(value)
                print(arraycreation)
        except NameError as e:
            print(e)

#To call the Array() function
Array()