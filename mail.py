import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
 
options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver =webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S1610909089%3A1690188006277766&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ifkv=AeDOFXiMe_mnBe8uyoQrmjjIRG6uGMPp4qrTRV1f7J8deVPZB7qZa2rwJw61AF9KVHnrAKI4l4oOJA&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.find_element(By.ID,"identifierId").send_keys("ganesh.nallabapineni@maangtechnologies.com")
driver.find_element(By.XPATH,"//button[contains(@class,'VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b')]").click()
driver.find_element(By.NAME,"Passwd").send_keys("gannumouni@143")
