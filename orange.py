from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://opensource-demo.orangehrmlive.com/")
search=driver.find_element(by=BY.NAME, value="username")
search.send_keys("Admin")
search=driver.find_element(by=BY.NAME, value="password")
search.send_keys("admin123")
search.send_keys(Keys.RETURN)


act_title=driver.title
exp_title="OrangeHRM"
if act_title==exp_title:
	print("login test passed")
else:
	print("faild test")
driver.close()
