'''
@Author: Santanu Mohapatra
@Date: 07/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 16:10 PM
@Title: Testing for Clinique Management System
'''

import unittest
from Doctor import *
from Patient import *

class TestCliniqueManagement(unittest.TestCase):
   
  
    def test_files(self):
        '''
        Description: Test the attributes of the file.
        Parameters: Json file attributes.
        Return: None.
        '''
        doctorList = Doctor()
        patientList = Patient()
        Doctors = doctorList.getDoctor()
        Patients = patientList.getPatient()
        for index in Doctors:
            list = Doctors[index]
            self.assertEqual(len(list) == 5)
        for index in Patients:
            list = Patients[index]
            self.assertEqual(len(list) == 2)
    
   
    def test_insertrecord(self):
        '''
        Description: Test the patient details that has been inserted to the file.
        Parameters: Patient details.
        Return: None.
        '''
        patientList = Patient()
        patientList.addPatient("Santanu", "6294476499", "22")
        Patients = patientList.getPatient()
        for index in Patients:
            list = Patients[index]
            self.assertEqual(len(list) == 3)

    def test_appointment(self):
        '''
        Description: Test the appointment details to the file.
        Parameters: appointment timing
        Return: None.
        '''
        patientList = Patient()
        doctorList = Doctor()
        patient_id = patientList.existingPatient("Nishruti")
        doctorList.makeAppointment(patient_id, 1)
        Doctors = doctorList.getDoctor()
        for index in Doctors: 
            list = Doctors[index]
            for j in range(len(list)):
                dict = list[j]
                if(dict['id'] == 1):
                    self.assertEqual(len(dict['patientList']) == 2)
    if __name__ == "__main__":
        unittest.main()     

