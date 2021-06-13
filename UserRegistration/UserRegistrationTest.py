'''
@Author: Santanu Mohapatra
@Date: 12/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 13:30 PM
@Title: PyTest for User Registration Problem
'''
from UserRegistration import *
import pytest

class Test_userRegistration:

    def test_first_name(self):

        userregistration = userRegistration()
        #firstnametest = userregistration.firstNameCheck(" ")
        assert userregistration.firstNameCheck() == "Santanu"

    def test_last_name(self):

        userregistration = userRegistration()
        #lastnametest = userregistration.lastNameCheck(" ")
        assert userregistration.lastNameCheck() == "Mohapatra"

    def test_email(self):

        userregistration = userRegistration()
        #emailtest = userregistration.eMailCheck(" ")
        assert userregistration.eMailCheck() == "mohapatra.santanu123@gmail.com"

    def test_mobile(self):

        userregistration = userRegistration()
        #mobiletest = userregistration.mobileNumberCheck(" ")
        assert userregistration.mobileNumberCheck() == "8675432190"

    def test_password(self):

        userregistration = userRegistration()
        #passwordtest = userregistration.passWordCheck(" ")
        assert userregistration.passWordCheck() == "Guddu@123"

    def test_wrong_password(self):
        userregistration = userRegistration()
        assert userregistration.passWordCheck() == "@123" 

if __name__=="__main__":
    Test_userRegistration()

