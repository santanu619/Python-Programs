'''
@Author: Santanu Mohapatra
@Date: 02/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 05:00 PM
@Title: Print the number of wins and percentage of win and loss by the gambler
'''
import random as r

#To take the input
try:
    stake = int(input("Enter the stake amount to start with: "))
    goal = int(input("Enter the goal amount to reach: "))
    number_of_time = int(input("Enter the number of times to run "))

except ValueError:
    print("Please enter the correct input")

  
#Define a function to run N number of times and bet stake until goal is reached or becomes zero.
try:
    def gambler():
        count=0
        win=0  
        for i in range(number_of_time):
            bet = stake  
            while bet > 0 and bet < goal:
                count += 1 
                if r.randint(0,1) == 0:
                    bet += 1
                else:
                    bet -= 1
               
            if bet == goal:
                win += 1
        print(win/number_of_time*100)
        print(bet) 
except NameError as e:
    print(e)

"""
A function to create the gambler problem where the gambler will bet and the function will print the number of times the gambler won.
Parameter:
Here count and win are the parameters taken.
"""
gambler()