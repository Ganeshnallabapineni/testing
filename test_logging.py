import logging

def test_loggingdemo(): 
	
	logger=logging.getLogger(__name__)
	fileHandler=logging.FileHandler('logfile.log')
	formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
	fileHandler.setFormatter(formatter)

	logger.addHandler(fileHandler)
	logger.setLevel(logging.INFO)

	logger.debug("A debug statement is executed")
	logger.info("information")
	logger.warning("something is in wrong mode")
	logger.error("a major error happened")
	logger.critical("critical issue")
	

