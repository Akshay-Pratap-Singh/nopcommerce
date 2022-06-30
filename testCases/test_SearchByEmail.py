import random
import string
import time

import pytest
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from selenium import webdriver

class Test_004_SearchCustomerByEmail:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen() #logger

    @pytest.mark.regression
    def test_SearchCustomerByEmail(self, setup):
        self.logger.info("*************** Test_003_AddCustomer ***************")
        self.driver = setup
        # self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*************** Login Successful ***************")

        self.logger.info("*************** Starting search customer by Email ***************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        time.sleep(3)

        self.emails = self.driver.find_elements(By.XPATH, "//tbody//tr//td[2]")
        self.validation = False
        for email in self.emails:
            if email.text == "steve_gates@nopCommerce.com":
                self.logger.info("*************** Email found ***************")
                self.driver.save_screenshot("C:\\Users\\Akshay\\PycharmProjects\\SeleniumHybridFramework\\Screenshots"
                                            + "\\test_SearchCustomerByEmail.png")
                self.validation = True
                assert True

        if self.validation == False:
            self.logger.error("*************** Email not found ***************")
            self.driver.save_screenshot("C:\\Users\\Akshay\\PycharmProjects\\SeleniumHybridFramework\\Screenshots"
                                        +"\\test_SearchCustomerByEmail.png")
            assert False

        self.driver.close()




