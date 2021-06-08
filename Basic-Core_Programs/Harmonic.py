'''
@Author: Santanu Mohapatra
@Date: 01/06/2021
@Title: To print the harmonic series
'''
from fractions import Fraction
try:
    index=1
    harmonic=1
    number=int(input("Enter the power of N"))
    for index in range(1,number+1):
        harmonic+=Fraction(1/index)
    print(harmonic)
except ValueError:
    print("Wrong Number")
