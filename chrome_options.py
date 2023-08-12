import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
 
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--start-maximized")
driver =webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

print(driver.title)
