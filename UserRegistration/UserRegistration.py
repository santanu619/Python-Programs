'''
@Author: Santanu Mohapatra
@Date: 12/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 11:10 AM
@Title: User Registration Problem
'''
import logging
import re


class userRegistration:
    
    def __init__(self):
        '''
        Descriptions: This init function is used to take the regex patterns.
        Parameters: Regex pattern.
        Return: None.
        '''
        self.firstname = "^[A-Z]{1}[a-zA-Z]{2,}$"
        self.lastname = "^[A-Z]{1}[a-zA-Z]{2,}$"
        self.email = "^[a-z0-9A-Z]+([._+-][a-z0-9A-Z]+)*[@][a-z0-9A-Z]+[.][a-zA-Z]{2,3}(.[a-zA-Z]{2})?$"
        self.mobile = "^[0-9]{10}$"
        self.password = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"

    def getRegexUserRegistration(self):
        '''
        This function is used to get all other methods.
        '''
        self.firstNameCheck()
        self.lastNameCheck()
        self.eMailCheck()
        self.mobileNumberCheck()
        self.passWordCheck()
    
    def firstNameCheck(self):
        '''
        Description: This function is used to match the first name using regex pattern.
        Parameters: Regex Pattern.
        Return: First Name.
        '''
        try:
            first_name = input("Enter your First Name:")
            if re.match(self.firstname, first_name):
                print("First Name is Valid.")
            else:
                print("First Name is Invalid.")
                self.firstNameCheck()

        except Exception as e:
            logging.error(e)

    def lastNameCheck(self):
        '''
        Description: This function is used to match the last name using regex pattern.
        Parameters: Regex Pattern.
        Return: Last Name.
        '''
        try:
            last_name = input("Enter your Last Name:")
            if re.match(self.lastname, last_name):
                print("Last Name is Valid.")
            else:
                print("Last Name is Invalid.")
                self.lastNameCheck()

        except Exception as e:
            logging.error(e)

    def eMailCheck(self):
        '''
        Description: This function is used to match the email using regex pattern.
        Parameters: Regex Pattern.
        Return: Email.
        '''
        try:
            e_mail = input("Enter your Email Id:")
            if re.match(self.email, e_mail):
                print("Email Id is Valid.")
            else:
                print("Email Id is Invalid.")
                self.eMailCheck()

        except Exception as e:
            logging.error(e)

    def mobileNumberCheck(self):
        '''
        Description: This function is used to match the mobile number using regex pattern.
        Parameters: Regex Pattern.
        Return: Mobile Number.
        '''
        try:
            mobile_number = input("Enter your Mobile Number:")
            if re.match(self.mobile, mobile_number):
                print("Mobile Number is Valid.")
            else:
                print("Mobile Number is Invalid.")
                self.mobileNumberCheck()

        except Exception as e:
            logging.error(e)

    def passWordCheck(self):
        '''
        Description: This function is used to match the password using regex pattern.
        Parameters: Regex Pattern.
        Return: Password.
        '''
        try:
            user_password = input("Enter your Password:")
            if re.match(self.password, user_password):
                print("Password is Valid.")
            else:
                print("Password is Invalid.")
                self.passWordCheck()

        except Exception as e:
            logging.error(e)

if __name__=="__main__":
    userregistration = userRegistration()
    print("-----WELCOME TO USER REGISTRATION CELL-----")
    userregistration.getRegexUserRegistration()