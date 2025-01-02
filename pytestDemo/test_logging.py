import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')

    formater = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

    fileHandler.setFormatter(formater)
    logger.addHandler(fileHandler)  # file handler object

    logger.setLevel(logging.DEBUG)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is in warning")
    logger.error("An error has occurred")
    logger.critical("Critical issue")



