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

        user = UserRegistration()
        firstnametest = user.firstNameCheck("Santanu")
        assert firstnametest == True

    def test_last_name(self):

         user = UserRegistration()
         lastnametest = user.lastNameCheck("Mohapatra")
         assert lastnametest == True

    def test_email(self):

         user = UserRegistration()
         emailtest = user.eMailCheck("mohapatra.santanu123@gmail.com")
         assert emailtest == True

    def test_mobile(self):

         user = UserRegistration()
         mobiletest = user.mobileNumberCheck("8897654328")
         assert mobiletest == True

    def test_password(self):

         user = UserRegistration()
         passwordtest = user.passWordCheck("Guddu@123")
         assert passwordtest == True

    def test_first_name_negative(self):

        user = UserRegistration()
        firstnametestnegative = user.firstNameCheck("S")
        assert firstnametestnegative == False

    def test_last_name_negative(self):

         user = UserRegistration()
         lastnametestnegative = user.lastNameCheck("M")
         assert lastnametestnegative == False

    def test_email_negative(self):

         user = UserRegistration()
         emailtestnegative = user.eMailCheck("sdfgfh")
         assert emailtestnegative == False

    def test_mobile_negative(self):

         user = UserRegistration()
         mobiletestnegative = user.mobileNumberCheck("88")
         assert mobiletestnegative == False

    def test_password_negative(self):

         user = UserRegistration()
         passwordtestnegative = user.passWordCheck("@123")
         assert passwordtestnegative == False

    