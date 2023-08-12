import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from home.student.Desktop.selenium_training.framwork.page_object import homepage
@pytest.mark.usefixtures("setup")
class TestOne:

	def test_e2e(self):
		page_object=homepage(driver)
		page_object.enter_username("gaina")	
#self.driver.find_element(By.ID,"user_name").send_keys("gaina")
		self.driver.find_element(By.NAME,"email").send_keys("ganika@gmail.com")
		self.driver.find_element(By.ID,"password").send_keys("412.26.17")
		self.driver.find_element(By.CSS_SELECTOR, "input[name='commit']").click()

