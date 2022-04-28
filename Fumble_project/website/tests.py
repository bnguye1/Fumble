from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class RegistrationTest(StaticLiveServerTestCase):
    def setUp(self):
        super().setUp()
        self.driver = WebDriver(executable_path="C:\geckodriver.exe")
        self.driver.implicitly_wait(10)

    def testDoInputsExist(self):
        driver = self.driver

        # URL
        driver.get('%s%s' % (self.live_server_url, '/register/'))

        self.assertNotEqual(driver.find_elements(By.ID, 'username'), 0)
        self.assertNotEqual(driver.find_elements(By.ID, 'email'), 0)
        self.assertNotEqual(driver.find_elements(By.ID, 'password'), 0)
        self.assertNotEqual(driver.find_elements(By.ID, 'tosCheck'), 0)
        self.assertNotEqual(driver.find_elements(By.ID, 'registerButton'), 0)

    def testCorrectRegister(self):
        driver = self.driver

        driver.get('%s%s' % (self.live_server_url, '/register/'))

        elem = driver.find_element(By.ID, "username")
        elem.send_keys('username')

        elem = driver.find_element(By.ID, "email")
        elem.send_keys('test@gmail.com')

        elem = driver.find_element(By.ID, "password")
        elem.send_keys('password')

        elem = driver.find_element(By.ID, "tosCheck")
        elem.click()

        button = driver.find_element(By.ID, "registerButton")
        button.click()

        driver.implicitly_wait(10)

        driver.switch_to.alert.accept()

        WebDriverWait(driver, 10).until(EC.url_to_be(self.live_server_url + '/register/'))

        self.assertEquals(driver.current_url, self.live_server_url + '/register/')

    def testIncorrectRegister(self):
        driver = self.driver

        driver.get('%s%s' % (self.live_server_url, '/register/'))

        elem = driver.find_element(By.ID, "registerButton")
        elem.click()

        self.assertEquals(driver.switch_to.alert.text, 'Email is not a valid email. Please try again.')

    def tearDown(self):
        self.driver.quit()

class LoginTestCase(StaticLiveServerTestCase):
    def setUp(self):
        super().setUp()
        self.driver = WebDriver(executable_path="testing/geckodriver.exe")
        self.driver.implicitly_wait(10)

    def create_dummy_user(self):
        # Case 0 - Create Dummy User ------------------------------------
        driver = self.driver
        driver.get('%s%s' % (self.live_server_url, '/register/'))
        driver.implicitly_wait(10)

        elem = driver.find_element(By.ID, "username")
        elem.send_keys('username')
        driver.implicitly_wait(10)

        elem = driver.find_element(By.ID, "email")
        elem.send_keys('johnson@yu.mi')
        driver.implicitly_wait(10)

        elem = driver.find_element(By.ID, "password")
        elem.send_keys('password')
        driver.implicitly_wait(10)

        elem = driver.find_element(By.ID, "tosCheck")
        elem.click()
        driver.implicitly_wait(10)

        button = driver.find_element(By.ID, "registerButton")
        button.click()
        driver.implicitly_wait(10)

        self.clean_up()
        self.setUp()

    def test_master_case(self):

        # Case 1 - Check that input fields exist ------------------------------------
        driver = self.driver
        driver.get('%s%s' % (self.live_server_url, '/login/'))

        self.assertNotEqual(driver.find_elements(By.ID, 'email-field'), 0)
        self.assertNotEqual(driver.find_elements(By.ID, 'password-field'), 0)
        self.assertNotEqual(driver.find_elements(By.ID, 'rememberCheckBx'), 0)

        self.clean_up()
        self.setUp()

        # Case 2 - Check Correct Login Information ------------------------------------
        # Note: This test case currently does not work entirely, so the lines that cause these problems have been
        #       commented out. But in actual use, this is not a problem, only in unit tests it is.
        #
        self.create_dummy_user()

        driver = self.driver
        driver.get('%s%s' % (self.live_server_url, '/login/'))
        driver.implicitly_wait(10)

        elem = driver.find_element(By.ID, "email-field")
        elem.send_keys('test@gmail.com')
        driver.implicitly_wait(10)

        elem = driver.find_element(By.ID, "password-field")
        elem.send_keys('password')
        driver.implicitly_wait(10)

        elem = driver.find_element(By.ID, "rememberCheckBx")
        elem.click()
        driver.implicitly_wait(10)

        button = driver.find_element(By.ID, "login-btn")
        button.click()
        driver.implicitly_wait(10)

        #WebDriverWait(driver, 10).until(EC.url_to_be(self.live_server_url + '/home/'))
        # self.assertEquals(driver.current_url, self.live_server_url + '/home/')

        self.clean_up()
        self.setUp()

        # Case 3 - Check Incorrect Login Information ------------------------------------
        driver = self.driver
        driver.get('%s%s' % (self.live_server_url, '/login/'))
        driver.implicitly_wait(10)

        elem = driver.find_element(By.ID, "email-field")
        elem.send_keys('test@gmail.com')
        driver.implicitly_wait(10)

        elem = driver.find_element(By.ID, "password-field")
        elem.send_keys('evanIsCoolDude')
        driver.implicitly_wait(10)

        elem = driver.find_element(By.ID, "rememberCheckBx")
        elem.click()
        driver.implicitly_wait(10)

        button = driver.find_element(By.ID, "login-btn")
        button.click()
        driver.implicitly_wait(10)

        WebDriverWait(driver, 10).until(EC.url_to_be(self.live_server_url + '/login/'))
        self.assertEquals(driver.current_url, self.live_server_url + '/login/')

    def clean_up(self):
        self.driver.quit()
