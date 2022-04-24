from django.test import TestCase
from selenium import webdriver


class RegistrationTest(TestCase):

    def testForm(self):
        selenium = webdriver.Chrome()
        # URL
        selenium.get('http://127.0.0.1:8000/register/')


