import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
 
options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver =webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
driver.find_element(By.ID,"username").send_keys("nbganesh2002@gmail.com")
driver.find_element(By.ID,"password").send_keys("gannumouni@143")
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
username=["CHINTA NARASIMHULU"]
length=len(username)
print(length)
for i in range(length):
	print(username[i])
	driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search']").send_keys(username[i])
	driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search']").send_keys(Keys.ENTER)

results=driver.find_elements(By.CSS_SELECTOR,"span[dir='ltr'] span")
count=len(results)
for result in results:
	if result.text=="username[i]":
		result.click()
		break
driver.find_element(By.XPATH,"((//button[contains(@aria-label,'Invite "+username[i]+" to connect')]//span[text()='Connect'])[2])").click()


driver.find_element(By.XPATH,"//button[contains(@aria-label,'Send now')]").click()




	

