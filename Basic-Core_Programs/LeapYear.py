'''
@Author: Santanu Mohapatra
@Date: 01/06/2021
@Title: Leap Year
'''
try:
    year=int(input("Enter the Year"))
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400 ) == 0:
                print(year, "is a leap year.")
            else:
                print(year, "is not a leap year.")
        else:
            print(year,"is a leap year.")
    else:
        print(year,"is not a leap year.")

except ValueError:
    print("Enter the correct Year")

