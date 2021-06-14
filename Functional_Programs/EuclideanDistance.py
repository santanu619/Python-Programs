'''
@Author: Santanu Mohapatra
@Date: 02/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 02:00 PM
@Title: To calculate the euclidean distance
'''
import math

try:
    x_coordinate = int(input("Enter the value of x coordinate "))
    y_coordinate = int(input("Enter the value of y coordinate "))
except ValueError: 
    print("Enter the correct input")
origin=0

#Create a function to calculate Euclidean distance
def euclideanDistance():
    try:
        euclideandistance = math.sqrt(math.pow(x_coordinate-origin,2)+math.pow(y_coordinate-origin,2))
        print(euclideandistance)
    except NameError as e:
        print(e)

#Call the function to calculate the euclidean distance              
euclideanDistance()