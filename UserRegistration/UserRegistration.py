'''
@Author: Santanu Mohapatra
@Date: 12/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 11:10 AM
@Title: User Registration Problem
'''
import logging
import re


class UserRegistration:
    
    def getRegexUserRegistration(self):
        '''
        This function is used to get all other methods.
        '''
        self.firstNameCheck()
        self.lastNameCheck()
        self.eMailCheck()
        self.mobileNumberCheck()
        self.passWordCheck()
    
    def firstNameCheck(self, first_name):
        '''
        Description: This function is used to match the first name using regex pattern.
        Parameters: Regex Pattern.
        Return: First Name.
        '''
        try:
            self.firstname = "^[A-Z]{1}[a-zA-Z]{2,}$"
            if re.match(self.firstname, first_name):
                logging.info("First Name is Valid.")
                return True
            else:
                 logging.info("First Name is Invalid.")
                 self.firstNameCheck()
                 return False

        except Exception as e:
           logging.error(e)

    def lastNameCheck(self, last_name):
        '''
        Description: This function is used to match the last name using regex pattern.
        Parameters: Regex Pattern.
        Return: Last Name.
        '''
        try:
            self.lastname = "^[A-Z]{1}[a-zA-Z]{2,}$"
            if re.match(self.lastname, last_name):
                logging.info("Last Name is Valid.")
                return True
            else:
                logging.info("Last Name is Invalid.")
                self.lastNameCheck()
                return False

        except Exception as e:
            logging.error(e)

    def eMailCheck(self, e_mail):
        '''
        Description: This function is used to match the email using regex pattern.
        Parameters: Regex Pattern.
        Return: Email.
        '''
        try:
            self.email = "^[a-z0-9A-Z]+([._+-][a-z0-9A-Z]+)*[@][a-z0-9A-Z]+[.][a-zA-Z]{2,3}(.[a-zA-Z]{2})?$"
            if re.match(self.email, e_mail):
                logging.info("Email Id is Valid.")
                return True
            else:
                logging.info("Email Id is Invalid.")
                self.eMailCheck()
                return False

        except Exception as e:
            logging.error(e)

    def mobileNumberCheck(self, mobile_number):
        '''
        Description: This function is used to match the mobile number using regex pattern.
        Parameters: Regex Pattern.
        Return: Mobile Number.
        '''
        try:
            self.mobile = "^[0-9]{10}$"
            if re.match(self.mobile, mobile_number):
                logging.info("Mobile Number is Valid.")
                return True
            else:
                logging.info("Mobile Number is Invalid.")
                self.mobileNumberCheck()
                return False

        except Exception as e:
            logging.error(e)

    def passWordCheck(self, user_password):
        '''
        Description: This function is used to match the password using regex pattern.
        Parameters: Regex Pattern.
        Return: Password.
        '''
        try:
            self.password = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
            if re.match(self.password, user_password):
                logging.info("Password is Valid.")
                return True
            else:
                logging.info("Password is Invalid.")
                self.passWordCheck()
                return False

        except Exception as e:
            logging.error(e)

if __name__=="__main__":
    userregistration = UserRegistration()
    print("-----WELCOME TO USER REGISTRATION CELL-----")
    userregistration.getRegexUserRegistration()