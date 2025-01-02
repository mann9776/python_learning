import inspect
import logging


class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logfile.log')

        formater = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        fileHandler.setFormatter(formater)
        logger.addHandler(fileHandler)  # file handler object

        logger.setLevel(logging.DEBUG)
        return logger