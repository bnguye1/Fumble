from django.test import TestCase
from selenium import webdriver


class RegistrationTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def testDoInputsExist(self):
        driver = self.driver

        # URL
        driver.get('localhost:8000/register/')

        self.assertNotEqual(driver.find_elements('usernameBox'), 0)
        self.assertNotEqual(driver.find_elements('emailBox'), 0)
        self.assertNotEqual(driver.find_elements('passwordBox'), 0)
        self.assertNotEqual(driver.find_elements('tosCheck'), 0)
        self.assertNotEqual(driver.find_elements('registerButton'), 0)

    def tearDown(self):
        self.driver.quit()


class DatabaseTest(TestCase):
    def simpleSelect(self):
        pass

