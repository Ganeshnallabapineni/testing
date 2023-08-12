import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
 
options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver =webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
#collect all vegie names
browsersorted=[]
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
webelements=driver.find_elements(By.XPATH,"//tr/td[1]")

for elements in webelements:
	browsersorted.append(elements.text)

originallist=browsersorted.copy()
browsersorted.sort()
assert browsersorted == originallist
