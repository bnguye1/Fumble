from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class RegistrationTest(StaticLiveServerTestCase):
    def setUp(self):
        super().setUp()
        self.driver = WebDriver()
        self.driver.implicitly_wait(10)

    def testDoInputsExist(self):
        driver = self.driver

        # URL
        driver.get('%s%s' % (self.live_server_url, '/register/'))

        self.assertNotEqual(driver.find_elements(By.ID, 'usernameBox'), 0)
        self.assertNotEqual(driver.find_elements(By.ID, 'emailBox'), 0)
        self.assertNotEqual(driver.find_elements(By.ID, 'passwordBox'), 0)
        self.assertNotEqual(driver.find_elements(By.ID, 'tosCheck'), 0)
        self.assertNotEqual(driver.find_elements(By.ID, 'registerButton'), 0)

    def testCorrectRegister(self):
        driver = self.driver

        driver.get('%s%s' % (self.live_server_url, '/register/'))

        elem = driver.find_element(By.ID, "usernameBox")
        elem.send_keys('username' + Keys.RETURN)

        elem = driver.find_element(By.ID, "emailBox")
        elem.send_keys('test@gmail.com' + Keys.RETURN)

        elem = driver.find_element(By.ID, "passwordBox")
        elem.send_keys('password' + Keys.RETURN)

        elem = driver.find_element(By.ID, "tosCheck")
        elem.click()

        button = driver.find_element(By.ID, "registerButton")
        button.click()

        driver.implicitly_wait(10)

        driver.switch_to.alert.accept()

        WebDriverWait(driver, 10).until(EC.url_to_be(self.live_server_url + '/login/'))

        self.assertEquals(driver.current_url, self.live_server_url + '/login/')

    def testIncorrectRegister(self):
        driver = self.driver

        driver.get('%s%s' % (self.live_server_url, '/register/'))

        elem = driver.find_element(By.ID, "registerButton")
        elem.click()

        self.assertEquals(driver.switch_to.alert.text, 'Email is not a valid email. Please try again.')

    def tearDown(self):
        self.driver.quit()
