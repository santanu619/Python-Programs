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

        user = userRegistration()
        firstnametest = user.firstNameCheck("Santanu")
        assert firstnametest == True

    def test_last_name(self):

         user = userRegistration()
         lastnametest = user.lastNameCheck("Mohapatra")
         assert lastnametest == True

    def test_email(self):

         user = userRegistration()
         emailtest = user.eMailCheck("mohapatra.santanu123@gmail.com")
         assert emailtest == True

    def test_mobile(self):

         user = userRegistration()
         mobiletest = user.mobileNumberCheck("8897654328")
         assert mobiletest == True

    def test_password(self):

         user = userRegistration()
         passwordtest = user.passWordCheck("Guddu@123")
         assert passwordtest == True

    def test_first_name_negative(self):

        user = userRegistration()
        firstnametestnegative = user.firstNameCheck("S")
        assert firstnametestnegative == True

    def test_last_name_negative(self):

         user = userRegistration()
         lastnametestnegative = user.lastNameCheck("M")
         assert lastnametestnegative == True

    def test_email_negative(self):

         user = userRegistration()
         emailtestnegative = user.eMailCheck("sdfgfh")
         assert emailtestnegative == True

    def test_mobile_negative(self):

         user = userRegistration()
         mobiletestnegative = user.mobileNumberCheck("88")
         assert mobiletestnegative == True

    def test_password_negative(self):

         user = userRegistration()
         passwordtestnegative = user.passWordCheck("@123")
         assert passwordtestnegative == True

    