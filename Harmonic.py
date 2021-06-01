'''
@Author: Santanu Mohapatra
@Date: 01/06/2021
@Title: To print the harmonic series
'''
from fractions import Fraction
try:
    number=int(input("Enter the power of N"))
except ValueError:
    print("Wrong Number")
N=1
harmonic=1
for N in range(1,number+1):
    harmonic+=Fraction(1/N)
print(harmonic)