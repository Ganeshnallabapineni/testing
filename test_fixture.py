import pytest
@pytest.mark.usefixtures("setup")
class TestExample:

	def test_fix(self):
		print("hello")
	
	def test_gan(self):
		print("hdth")
	

