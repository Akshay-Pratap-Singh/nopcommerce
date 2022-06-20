import os
import time
import pytest

from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("*************** Test_001_Login ***************")
        self.logger.info("*************** Verifying Home Page title ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        act_title = self.driver.title
        if act_title == "Your store. Login":
            # Added 123 after act_title to get this failed
            self.driver.close()
            self.logger.info("*************** Home Page Title test is passed ***************")
            assert True
        else:
            # self.driver.save_screenshot(os.getcwd()+"\\test_homePageTitle.png")
            self.driver.save_screenshot("C:\\Users\\Akshay\\PycharmProjects\\SeleniumHybridFramework\\Screenshots"+"\\test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*************** Home Page Title test is failed ***************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration123":
            # Added 123 after act_title to get this failed
            self.driver.close()
            self.logger.info("*************** Log in test is passed ***************")
            assert True
        else:
            # self.driver.save_screenshot(os.getcwd()+"\\test_login.png")
            self.driver.save_screenshot("C:\\Users\\Akshay\\PycharmProjects\\SeleniumHybridFramework\\Screenshots"+"\\test_login.png")
            self.driver.close()
            self.logger.error("*************** Log in test is failed ***************")
            assert False




