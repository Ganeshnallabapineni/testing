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
driver.get("https://sso.teachable.com/secure/9521/identity/sign_up/email")
driver.find_element(By.ID,"user_name").send_keys("gaina")
driver.find_element(By.NAME,"email").send_keys("ganika@gmail.com")
driver.find_element(By.ID,"password").send_keys("412.26.17")
driver.find_element(By.CSS_SELECTOR, "input[name='commit']").click()

