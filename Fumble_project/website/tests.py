from django.test import TestCase
from django.test import override_settings, TestCase
from contextlib import contextmanager
from django.urls import reverse, resolve
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from django.test import SimpleTestCase
from .models import User
from .models import Team
from .views import navbar


class RegistrationTest(StaticLiveServerTestCase):
    def setUp(self):
        super().setUp()
        self.driver = WebDriver(executable_path="testing/geckodriver.exe")
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

        WebDriverWait(driver, 10).until(EC.url_to_be(self.live_server_url + '/login/'))

        self.assertEquals(driver.current_url, self.live_server_url + '/login/')

        self.assertIs(User.objects.filter(email="test@gmail.com").exists(), True)

    def testIncorrectRegister(self):
        driver = self.driver

        driver.get('%s%s' % (self.live_server_url, '/register/'))

        elem = driver.find_element(By.ID, "registerButton")
        elem.click()

        driver.switch_to.alert.accept()

        self.assertEquals(driver.current_url, self.live_server_url + '/register/')

    def tearDown(self):
        self.driver.quit()

# Testing database queries


class DatabaseTest(TestCase):
    def setUp(self):
        User.objects.create(isCapt=False, locationX=20, locationY=40, teamName="Tigers",
                            password="hashed",email="myemail@email")
        User.objects.create(isCapt=True, locationX=20, locationY=40, teamName="Lions",
                            password="hashing",email="myemail@gmail")
        User.objects.create(isCapt=False, locationX=20, locationY=40, teamName="Bears",
                            password="slasher",email="myemail@aol")

    def testRetrieve(self):
        try:
            captain = User.objects.get(isCapt=True)
        except Exception:
            print("could not find a captain")

        try:
            aPlayer = User.objects.get(password="slasher")
        except Exception:
            print("could not find user with password \"slasher\"")

        # did we get a captain?
        try:
            self.assertEqual(captain.isCapt, True)
        except Exception:
            print("could not retrieve a captain")

        # did we retrieve this user's password?
        try:
            self.assertEqual(aPlayer.password, "slasher")
        except Exception:
            print("could not retrieve player with password \"slasher\"")


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

class TestPages(SimpleTestCase):
    def testNavBar(self):
        # Test whether the URL routes correctly to the navigation bar.
        url = reverse('navigation-bar')
        self.assertEquals(resolve(url).func, navbar)

        # Use Selenium to test whether the proper elements are present on the page
        driver = webdriver.Firefox()
        driver.get("http://127.0.0.1:8000/navbar/")

        # Locating the Navigation bar
        potential_bar = driver.find_element(By.CLASS_NAME, "pages")

        # Locating the logos
        potential_astley = driver.find_element(By.CLASS_NAME, "astley")
        potential_ben = driver.find_element(By.CLASS_NAME, "ben")

    def testMap(self):
        # Test whether the URL routes correctly to the map page.
        url = reverse('website-map')
        self.assertEquals(resolve(url).func, map)

        # Use Selenium to ensure that the map element is present.
        driver = webdriver.Firefox()
        driver.get("http://127.0.0.1:8000/map/")
        potential_map = driver.find_element(By.ID, "map")
