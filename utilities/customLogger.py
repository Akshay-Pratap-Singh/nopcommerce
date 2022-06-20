import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        # logging.basicConfig(filename= os.getcwd()+"\\automation.log",
        #                     format="%(asctime)s: %(levelname)s: %(message)s",
        #                     datefmt= "%m%d%Y %I:%M:%S %p"
        #                     )

        # logger = logging.getLogger()

        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('C:\\Users\\Akshay\\PycharmProjects\\SeleniumHybridFramework\\Logs\\automation.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger


