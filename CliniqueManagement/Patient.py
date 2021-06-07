'''
@Author: Santanu Mohapatra
@Date: 06/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 17:50 PM
@Title: Patient class for Clinique Management System
'''

import os
import json
from Doctor import *

class Patient:
    #Created a list to store the details of doctors
    Patients = {}
    def __init__(self):
        if os.path.isfile("Doctor.json"):
            with open("Patient.json", "r") as f:
                self.Patients = json.load(f)

    """
    Function to add patients in the database.
    Parameters: The attributes of the patient's json file are taken as parameters.
    Return type: None.
    """
    def addPatient(self, name, phone_number, age):
        for i in self.Patients:
            list = self.Patients[i]
            dict = {}
            dict['name'] = name
            dict['id'] = len(list) + 1
            dict['phone_number'] = phone_number
            dict['age'] = age
            list.append(dict)

    """
    Function to check for existing patients in the database.
    Return type: Patient name.
    """
    def existingPatient(self, name):
        for i in self.Patients:
            list = self.Patients[i]
            for j in range(len(list)):
                dict = list[j]
                if (dict['name'] == name):
                    return dict['id']

    """
    Functions to print the details of the patient.
    Parameters: Details from the Json file of the doctor.
    Return: None.
    """
    def printPatient(self):
       for i in self.Patients:
            list = self.Patients[i]
            for j in range(len(list)):
                dict = list[j]
                print("------------------------------------------")
                print("name: {}".format(dict['name']))
                print("id: {}".format(dict['id']))
                print("------------------------------------------")
    """
    Functions to save the entries into the json file.
    Parameters: New Entries.
    Return: None
    """
    def save_to_json(self):
        with open("Patient.json", "w") as f:
                json.dump(self.Patients, f, indent=4)

    def getPatient(self):
        return self.Patients
