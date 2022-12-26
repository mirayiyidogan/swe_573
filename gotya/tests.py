from django.test import TestCase

# Create your tests here.
from .models import *
from django.contrib.auth import authenticate

class UserAuthanticationTest(TestCase):

    def test_login(self):
        user= authenticate(email="miray.iyidogan", password="test_1234")
        self.assertTrue(user is not None) and user.is_authanticated
    
    def test_password_wrong(self):
        user= authenticate(email="miray.iyidogan", password="false")
        self.assertFalse(user is not None and user.is_authanticated)
    
    def test_username_wrong(self):
        user= authenticate(email="xxx", password="test_1234")
        self.assertFalse(user is not None and user.is_authanticated)


    
