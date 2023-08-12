#any pytest file start with test_ or end with _test
#pytest method name shold start with test
#py.test -v -s[for printing all tests]
#-k stands for method names execution -s logs iin out pput -v stands for more info metadata
#you can run specific file with py.test <filename>
#you can mark tests @pytest.mark.smoke and then run with -m
#you can skip tests with @pytest.mark.skip
#@pytest.mark.xfail
#fixtures are used as setup and tear down methods for test cases-conftest file to generalize 
#fixture and make it available to all test cases(fixture name into parameter of method)
# datadriven and parameteriation can be done wiith return statements in tuple format
#when you define the fixture scope to class only,it will run once before class is initiated and at the end  


def test_firstprogram():
	print("hello")
def test_secondname():
	print("gaina")
