from django.test import TestCase
from selenium import webdriver


class RegistrationTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        pass

    def testDoInputsExist(self):
        driver = self.driver

        # URL
        driver.get('http://127.0.0.1:8000/register/')

        self.assertNotEqual(driver.find_elements('usernameBox'), 0)
        self.assertNotEqual(driver.find_elements('emailBox'), 0)
        self.assertNotEqual(driver.find_elements('passwordBox'), 0)
        self.assertNotEqual(driver.find_elements('tosCheck'), 0)
        self.assertNotEqual(driver.find_elements('registerButton'), 0)

        driver.close()

    def tearDown(self):
        self.driver.close()
