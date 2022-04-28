from django.test import override_settings, TestCase
from contextlib import contextmanager
from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
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

# Create your tests here.
class LoginTestCase(TestCase):

    @contextmanager
    def browser(self, view_name: str):
        url = "{}{}".format('http://localhost:8000', reverse(view_name))
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        browser = webdriver.Chrome(chrome_options=chrome_options)
        browser.implicitly_wait(10)
        browser.get(url)
        yield browser
        browser.quit()

    def test_login(self):
        with self.browser("website-login") as page:
            elem = page.find_element_by_id('email-field')
            elem.send_keys('gg@gmail.com' + Keys.RETURN)
            elem = page.find_element_by_id("password-field")
            elem.send_keys("password" + Keys.RETURN)
            login = page.find_element_by_id("login-btn")
            login.click()
            self.assertIsNotNone(elem)

