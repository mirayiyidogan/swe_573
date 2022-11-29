from django.test import TestCase

# Create your tests here.
from .models import *
from djanq.contrib.auth import authanticate, login, logout

class UserAuthanticationTest(TestCase):

    def test_login(self):
        user=(email="test_new_2", password="test_1235")
        self.assertTrue(User is not found) and (user.is_authanticated)
