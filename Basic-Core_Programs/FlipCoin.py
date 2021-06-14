'''
@Author: Santanu Mohapatra
@Date: 01/06/2021
@Title: Flip Coin and print percentage of Heads and Tails
'''
import random
head=0
tail=0
try: 
    number=int(input("Enter the number of times to flip the coin:"))
    print("HEADS or TAILS")
    if number < 0:
        print("Wrong Number")
    else:
        for x in range(0,number):
            flip=random.random()
            if flip < 0.5:
                tail+=1
            else:
                head+=1
    head_percent=(head/number)*100
    tail_percent=(tail/number)*100
    print("Number of Heads:", head)
    print("Number of Tails:", tail)
    print("Percentage of Head:", head_percent)
    print("Percentage of Tail:", tail_percent)
except ValueError:
    print("Please give the correct number")

