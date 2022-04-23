from django.test import override_settings, TestCase
from contextlib import contextmanager
from django.urls import reverse
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


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
