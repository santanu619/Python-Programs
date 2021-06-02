'''
@Author: Santanu Mohapatra
@Date: 01/06/2021
@Title: Power of 2
'''
power=1
MultiplicationPower=2
try:
    number=int(input("Enter the power value of N"))
    if 0 < number < 31:
        for x in range(0,number):
            power=(power*MultiplicationPower)
            print(power)
    else:
        print("Power is out of range. Give another number.")
except ValueError:
    print("Enter the correct number")
