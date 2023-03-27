import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver =webdriver.Chrome(ChromeDriverManager().install())
 
driver.get('http://www.google.com')
search = driver.find_element(by=By.NAME, value="q")
search.send_keys("automation step by step")
search.send_keys(Keys.RETURN)
 
time.sleep(5)
driver.close()
