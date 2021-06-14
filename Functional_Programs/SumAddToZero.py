'''
@Author: Santanu Mohapatra
@Date: 01/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 12:45 PM
@Title: To print sum of three integers which adds to zero
'''
try:
    number = int(input("Enter the number of integers "))
except:
    print("Enter a positive integer value")

#To create a array and check for the input
array = []
for i in range(number):
    try:
        value = int(input("Enter the value  "))
    except ValueError:
        print("Enter correct integer value")
    array.append(value)

#To check the sum of array values in triples is zero 
def sumOfIntegers():
    try: 
        index=0
        for i in range(0, number-2):
            for j in range(i+1,number-1):
                for k in range(j+1, number):
                    if(array[i] + array[j] + array[k] == 0):
                        print(array[i], array[j], array[k])
                        index += 1
        print("The number of triple pairs equal to zero are ", index)  
    except NameError as e:
        print(e) 
#Call the function to print the triplets
sumOfIntegers()

