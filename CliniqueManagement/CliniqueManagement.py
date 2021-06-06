'''
@Author: Santanu Mohapatra
@Date: 06/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 09:40 AM
@Title: Clinique Management System
'''

import os
import re
import logging
import json

#Set environment variables
USERNAME = input("Enter the username to proceed:\n")
os.environ['INVENTORY_MANAGER'] = USERNAME
USER_PASSWORD = input("Enter the password:\n")
os.environ['PASSWORD'] = USER_PASSWORD

#Get environment variables
USER=os.getenv('INVENTORY_MANAGER')
PASSWORD=os.environ.get('PASSWORD')

class CliniqueManagement:
    
    #Created a list to store the details of doctors and patients
    Doctor = {}
    Patient = {}

    def __init__(self):
        if os.path.isfile("Doctors.json"):
            with open("Doctors.json", "r") as f:
                self.Doctor = json.load(f)
        if os.path.isfile("Doctors.json"):
            with open("Patients.json", "r") as f:
                self.Patient = json.load(f)
    """
    Function to add patients in the database.
    """
    def addPatient(self, name, phone_number, age):
       
        
        for i in self.Patient:
            list = self.Patient[i]
            dict = {}
            dict['name'] = name
            dict['id'] = len(list) + 1
            dict['phone_number'] = phone_number
            dict['age'] = age
            list.append(dict)

    """
    Function to check for existing patients in the database.
    """
    def existingPatient(self, name):
        for i in self.Patient:
            list = self.Patient[i]
            for j in range(len(list)):
                dict = list[j]
                if (dict['name'] == name):
                    return dict['id']

    def printDoctor(self):
       
        for i in self.Doctor:
            list = self.Doctor[i]
            for j in range(len(list)):
                dict = list[j]
                print("------------------------------------------")
                print("name: {}".format(dict['name']))
                print("id: {}".format(dict['id']))
                print("availability: {}".format(dict['availability']))
                print("specialization: {}".format(dict['specialization']))
                print("------------------------------------------")

    def printPatient(self):
       
        for i in self.Patient:
            list = self.Patient[i]
            for j in range(len(list)):
                dict = list[j]
                print("------------------------------------------")
                print("name: {}".format(dict['name']))
                print("id: {}".format(dict['id']))
                print("------------------------------------------")

    """
    Functions to make appointment by the patients.
    """
    def makeAppointment(self, patient_id, doctor_id):
        for i in self.Doctor:
            list = self.Doctor[i]
            for j in range(len(list)):
                dict = list[j]
                if(dict['id'] == doctor_id):
                    if(len(dict['patientList']) < 6):
                        dict['patientList'].append(patient_id)
                        print("Appointment booked on time.")
                    else:
                        print("Sorry the slots are full.")              

    def save_to_json(self):
        with open("Doctors.json", "w") as f:
                json.dump(self.Doctor, f, indent=4)

        with open("Patients.json", "w") as f:
                json.dump(self.Patient, f, indent=4)

    def getPatient(self):
        return self.Patient

    def getDoctor(self):
        return self.Doctor

def names(x):
    while True:
        try:
            name = input(x)
            pattern = "^[A-Z]{1}[a-zA-Z]{2,}$"
            result = re.match(pattern, name)
            if (result):
                return str(name)
        except:
            pass
        logging.warning("Give correct Name!")

def ages(x):
    while True:
        try:
            age = input(x)
            pattern = "^([1-9][0-9]{,8})$"
            result = re.match(pattern, age)
            if (result):
                return int(age)
        except:
            pass
        logging.warning("Avoid spaces between numbers")

def phones(x):
    while True:
        try:
            phone = input(x)
            pattern = "^[0-9]{10}$"
            result = re.match(pattern, phone)
            if (result):
                return str(phone)
        except:
            pass
        logging.warning("Enter proper Number")

"""
Description: clinique() function is considered as main function which is used to ask the entries by the users and make choices and here there is a admin login system and if the admin use correct login credentials, it will enter into the database of clinique management system.
"""        

def clinique():
    try:
        clinique = CliniqueManagement()
        user_input = ""
        print("|---------------------------------------------------------------|")
        print("***********    **************   ***********   **********")
        print("WELCOME TO CLINIQUE MANAGEMENT SYSTEM")
        print("***********    **************   ***********   **********")
        print("|---------------------------------------------------------------|")
        
        if USER == "santanu1213" and PASSWORD == "mymother@123":
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
                    clinique.addPatient(name, phone, age)
                    patient_id = clinique.existingPatient("Nihar")
                    clinique.printPatient()
                    choose_id = int(input("Please choose the ID of doctor to check for consultation: "))
                    clinique.makeAppointment(patient_id, choose_id)

                elif (user_input == "2"):
                    name = names("Enter patient name: ")
                    patient_id = clinique.existingPatient(name)
                    clinique.printPatient()
                    choose_id = int(input("Please choose the ID of doctor to check for consultation: "))
                    clinique.makeAppointment(patient_id, choose_id)

                elif (user_input == "3"):
                    clinique.printDoctor()

                elif (user_input == "4"):
                    clinique.save_to_json()

                elif (user_input == "e"):
                    break

                else:
                    print("Choose correct options")
        else:
            print("Wrong Username and Password.......")
    except:
            pass

clinique()