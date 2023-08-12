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
 
options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver =webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,"input[class='search-keyword']").send_keys("ber")
time.sleep(2)
expected=['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
actuallist=[]
results=driver.find_elements(By.XPATH,"//div[@class='products']/div")
count=len(results)
print(count)

for result in results:
	actuallist.append(result.find_element(By.XPATH,"h4").text)
	result.find_element(By.XPATH,"div/button").click()
print(actuallist)
assert expected==actuallist
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
time.sleep(5)
#wait=WebDriverWait(driver,10)
#wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

prices=driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum=0
for price in prices:
	sum=sum+int(price.text)
print(sum)

totalamount=int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
print(totalamount)





















