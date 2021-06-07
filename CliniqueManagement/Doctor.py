'''
@Author: Santanu Mohapatra
@Date: 06/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 17:50 PM
@Title: Doctor class for Clinique Management System
'''

import os
import json
from Patient import *
class Doctor:

    #Created a list to store the details of doctors
    Doctor = {}
    def __init__(self):
        if os.path.isfile("Doctor.json"):
            with open("Doctor.json", "r") as f:
                self.Doctor = json.load(f)

    """
    Functions to print the details of the doctor.
    Parameters: Details from the Json file of the doctor.
    Return: None.
    """
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
    
    """
    Functions to make appointment by the patients.
    Parameters: List of existing and new patients.
    Return: None
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

    """
    Functions to save the entries into the json file.
    Parameters: New Entries.
    Return: None
    """
    def save_to_json(self):
        with open("Doctors.json", "w") as f:
                json.dump(self.Doctor, f, indent=4)

    def getDoctor(self):
        return self.Doctor