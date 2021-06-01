'''
@Author: Santanu Mohapatra
@Date: 01/06/2021
@Title: Power of 2
'''
power=1
N=2
try:
    number=int(input("Enter the power value of N"))
except ValueError:
    print("Enter the correct number")
if 0 < number < 31:
    for x in range(0,number):
        power=(power*N)
        print(power)
else:
    print("Power is out of range. Give another number.")