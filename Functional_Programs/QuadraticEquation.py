'''
@Author: Santanu Mohapatra
@Date: 02/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 02:30 PM
@Title: To find the quadratic equation
'''
from math import pow
from math import sqrt

try:
    a = int(input("Enter the value of a"))
    b = int(input("Enter the value of b"))
    c = int(input("Enter the value of c"))
except ValueError:
    print("Enter the correct input")

#Define a  Function to calculate the roots of the quadratic equation
def quadraticEquation():
    try:
        delta = pow(b,2)-(4*a*c)
        root1 = (-b+sqrt(delta))/(2*a)
        root2 = (-b-sqrt(delta))/(2*a)
        print(root1)
        print(root2)
    except NameError as e:
        print(e) 

#Call the function quadraticEquation() to find the value
quadraticEquation()
   