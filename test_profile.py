import pytest
from seltraining.BaseClass import BaseClass

@pytest.mark.usefixtures("dataload")
class TestExample2(baseclass):
	def test_profile(self,dataload):
		log=self.getlogger()
		
		log.info(dataload[0])
		log.info	(dataload[1])
def test_browser(browser):
	print(browser[1])
