'''
@Author: Santanu Mohapatra
@Date: 04/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 18:40 PM
@Title: Inventory Management Problem
'''

import json
#import os
import logging
#from decouple import config

# #Use logger handler
# logging.basicConfig(filename='Inventory_management.log', level=logging.CRITICAL, format='%(asctime)s-%(levelname)s-%(message)s')
# FILE_NAME=config('Inventory_Management')
# #Set environment variables
# USERNAME = input("Enter the username to proceed:\n")
# os.environ['INVENTORY_MANAGER'] = USERNAME
# USER_PASSWORD = input("Enter the password:\n")
# os.environ['PASSWORD'] = USER_PASSWORD

# #Get environment variables
# USER=os.getenv('INVENTORY_MANAGER')
# PASSWORD=os.environ.get('PASSWORD')

class Inventory:

    def __init__(self):
        pass

    """
    Description: Function defined to read the inventory management details from Json files and calculated its total price and write the details to Json files as well.
    Parameters: Weights and cost_per_kg are considered as parameters here.
    """

    def invertory_details(self):
    
        try:
           #Reading from Json File.
            with open(r"Inventory.json", "r") as file:     
                data = json.load(file)
        except Exception as e:
            logging.critical(e)

        rice_list=data['rice']
        for rice_total in range(len(rice_list)):
            rice = rice_list[rice_total].get("weight") * rice_list[rice_total].get("price_per_kg")

        pulses_list=data['pulses']        
        for pulses_total in range(len(pulses_list)):
            pulses = pulses_list[pulses_total].get("weight") * pulses_list[pulses_total].get("price_per_kg")

        wheat_list=data['wheat']
        for wheat_total in range(len(wheat_list)):
            wheat = wheat_list[wheat_total].get("weight") * wheat_list[wheat_total].get("price_per_kg")
        
        """
        Calculated the total cost of rice, wheats and pulses if the username and the password matches.
        """
        #if USER == "santanu1213" and PASSWORD == "mymother@123":
        print("Total value of rice is:", rice)
        print("Total value of pulse is:", pulses)
        print("Total value of wheat is:", wheat)    
        #else:
         #   print("Wrong Username and Password")
        try:
            #Writing to Json File
            with open(r"Next_Inventory.json", "w") as write_file:
                json.dump(data, write_file,indent=3)
        except Exception as e:
            logging.critical(e)
        


if __name__ == "__main__": 
    inventory = Inventory()           
    inventory.invertory_details()            