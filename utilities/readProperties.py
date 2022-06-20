import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\Akshay\\PycharmProjects\\SeleniumHybridFramework\\Configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get("common info", "baseURL")
        return url

    @staticmethod
    def getUserEmail():
        useremail = config.get("common info", "useremail")
        return useremail

    @staticmethod
    def getPassword():
        password = config.get("common info", "password")
        return password