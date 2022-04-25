from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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

    def testCorrectRegister(self):
        driver = self.driver

        driver.get('localhost:8000/register/')

        elem = driver.find_element("usernameBox")
        elem.send_keys('username' + Keys.RETURN)

        elem = driver.find_element("emailBox")
        elem.send_keys('test@gmail.com' + Keys.RETURN)

        elem = driver.find_element("passwordBox")
        elem.send_keys('password' + Keys.RETURN)

        elem = driver.find_element("tosCheck")
        elem.click()

        elem = driver.find_element("registerButton")
        elem.click()

        driver.switch_to.alert.accept()

        driver.implicitly_wait(10)

        self.assertEquals(driver.current_url, "localhost:8000/login/")

    def tearDown(self):
        self.driver.quit()
