'''
@Author: Santanu Mohapatra
@Date: 02/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 03:00 PM
@Title: To print the wind chill
'''
import math

try:
    temperature = int(input("Enter the temperature in Fahrenheit(F):"))
    velocity = int(input("Enter the speed in miles per hour(MPH):"))
except:
    print("Enter the correct input!")

#Define a function to calculate the wind chill 
def windChill():
    try:
        windChill = (35.74 + 0.6215*temperature + (0.4275*temperature - 35.75)*math.pow(velocity,0.16))
        print(windChill)
    except NameError as e:
        print(e)

#Call the function windChill() to get the value
windChill()    