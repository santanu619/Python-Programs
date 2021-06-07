'''
@Author: Santanu Mohapatra
@Date: 07/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 17:00 PM
@Title: Main function class for Clinique Management System
'''

import re
import logging
import os
from Doctor import *
from Patient import *
from decouple import config

#Set environment variables
API_USERNAME = config('USER')
API_KEY = config('KEY')
#Get environment variables
USER=os.getenv('API_USERNAME')
PASSWORD=os.environ.get('API_KEY')

"""
Functions to enter the name of patient.
Parameters: Regex pattern.
Return: None.
"""
def names(patient_name):
    while True:
        try:
            name = input(patient_name)
            pattern = "^[A-Z]{1}[a-zA-Z]{2,}$"
            result = re.match(pattern, name)
            if (result):
                return str(name)
        except:
            pass
            logging.warning("Give correct Name!")

"""
Functions to enter the age of patient.
Parameters: Regex pattern.
Return: None.
"""
def ages(patient_age):
    while True:
        try:
            age = input(patient_age)
            pattern = "^([1-9][0-9]{,8})$"
            result = re.match(pattern, age)
            if (result):
                return int(age)
        except:
            pass
            logging.warning("Avoid spaces between numbers")

"""
Functions to enter the phone number of patient.
Parameters: Regex pattern.
Return: None.
"""
def phones(patient_phone):
    while True:
        try:
            phone = input(patient_phone)
            pattern = "^[0-9]{10}$"
            result = re.match(pattern, phone)
            if (result):
                return str(phone)
        except:
            pass
            logging.warning("Enter proper Number")

"""
Description: clinique() function is considered as main function which is used to ask the entries by the users and make choices and here there is a admin login system and if the admin use correct login credentials, it will enter into the database of clinique management system.
Paramters: All the objects of the json file and a choice constraint is considered as parameters.
Return Type: None
"""      
def CliniqueManagement():
    try:
        doctor = Doctor()
        patient = Patient()

        user_input = ""
        print("|---------------------------------------------------------------|")
        print("***********    **************   ***********   **********")
        print("WELCOME TO CLINIQUE MANAGEMENT SYSTEM")
        print("***********    **************   ***********   **********")
        print("|---------------------------------------------------------------|")
            
        while user_input != 'q':
            print("1 - New Patient")
            print("2 - Existing Patient")
            print("3 - Doctors List")
            print("4 - Write to JSON File")
            print("e - Exit")
            user_input = input("Select Option: ")

            if (user_input == "1"):
                name = names("Enter patient name: ")
                phone = phones("Enter patient number: ")
                age = ages("Enter patient age: ")
                patient.addPatient(name, phone, age)
                patient_id = patient.existingPatient(name)
                patient.printPatient()
                choose_id = int(input("Please choose the ID of doctor to check for consultation: "))
                doctor.makeAppointment(patient_id, choose_id)

            elif (user_input == "2"):
                name = names("Enter patient name: ")
                patient_id = patient.existingPatient(name)
                patient.printPatient()
                choose_id = int(input("Please choose the ID of doctor to check for consultation: "))
                doctor.makeAppointment(patient_id, choose_id)

            elif (user_input == "3"):
                doctor.printDoctor()

            elif (user_input == "4"):
                doctor.save_to_json()
                patient.save_to_json()

            elif (user_input == "e"):
                break

            else:
                print("Choose correct options")
            
    except:
        pass

CliniqueManagement()