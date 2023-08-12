import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
	

@pytest.fixture(scope="class")
def setup(request):
	browser_name=request.config.getoption("browser_name")
	if browser_name == "chrome":

		driver =webdriver.Chrome(ChromeDriverManager().install())
	elif browser_name == "firefox":
		
		driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

	driver.get("https://sso.teachable.com/secure/9521/identity/sign_up/email")
	driver.maximize_window()
	request.cls.driver=driver
	yield
	driver.close()
