from django.test import SimpleTestCase
from django.urls import reverse, resolve
from website.views import navbar, map
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestPages(SimpleTestCase):
	def testNavBar(self):
		# Test whether the URL routes correctly to the navigation bar. 
		url = reverse('navigation-bar')
		self.assertEquals(resolve(url).func, navbar)
		
		# Use Selenium to test whether the proper elements are present on the page
		driver = webdriver.Firefox()
		driver.get("http://127.0.0.1:8000/navbar/")
		
		#Locating the Navigation bar
		potential_bar = driver.find_element(By.CLASS_NAME, "pages")
		
		#Locating the logos
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
