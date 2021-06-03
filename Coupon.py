'''
@Author: Santanu Mohapatra
@Date: 02/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 11:40 PM
@Title: To print the distinct coupons
'''
import random

coupon = open("coupons.txt", "a")

#Define a function generate() to generate coupon codes
def generate(amount):
    try:
        for x in range(0, amount):

            a = random.randint(1, 100)
            a = str(a)
            b = random.randint(1, 100)
            b = str(b)
            c = random.randint(1, 100)
            c = str(c)

            total = ""
            total = str(total)
            total = a + " " + b + " " + c

            coupon.write(total)
            coupon.write("\n")
    except ValueError:
        print("Error in writing to text file")

amount = int(input("How many coupons do you want to generate: "))

"""
A function to generate the distinct coupon.
Parameter:
3 different coupon box a,b,c are taken as parameters.
"""
generate(amount)

coupon.close()

print("\nCoupon's have been generated!")
print(coupon)