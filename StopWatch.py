'''
@Author: Santanu Mohapatra
@Date: 02/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 05:40 PM
@Title: Print the elapsed time in the stop watch
'''
import time

begin_time=0
end_time=0

#Define the function to print the elapsed time in  stop watch
try:
    def stopWatch():
        begin_time = input("Press enter to start the watch")
        begin_time=time.time()
        end_time = input("Stop the watch")
        end_time=time.time()
        elapsedtime = end_time - begin_time
        print(elapsedtime)   
except ValueError:
    print("Please enter the correct input")

#Call the function stopwatch() to calculate and print the elapsed time
stopWatch()