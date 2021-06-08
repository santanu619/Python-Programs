'''
@Author: Santanu Mohapatra
@Date: 01/06/2021
@Title: To get the prime factors of number N
'''
try:
    number=int(input("Enter the number:"))
    for index in range(2,number):
        while(number%index==0):
            print(index)
            number=number/index
            print(number)
except ValueError:
    print("Please enter the correct number")
