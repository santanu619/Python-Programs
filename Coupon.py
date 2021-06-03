import random

coupon = open("coupons.txt", "a")

def generate(amount):

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


amount = int(input("How many coupons do you want to generate: "))

generate(amount)

coupon.close()

print("\nCode's have been generated!")
print(coupon)