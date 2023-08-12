import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver =webdriver.Chrome(ChromeDriverManager().install())
 
driver.get('https://www.amazon.in/')
driver.find_element(by=By.ID,value="twotabsearchtextbox").send_keys("laptop")
driver.find_element(By.ID,"nav-search-submit-button").click()
 
time.sleep(5)
driver.close()
