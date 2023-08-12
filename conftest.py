import pytest
@pytest.fixture(scope="class")
def setup():
	print("excuting")
	yield
	print("excuted")

@pytest.fixture(scope="class")
def dataload():
	print("users data")
	return["gannu","mouni"]

@pytest.fixture(params=[("chrome","gannu"),("firefox","mouni"),("opera","nb")])
def browser(request):
	return request.param

