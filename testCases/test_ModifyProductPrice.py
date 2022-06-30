import random
import string
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.LoginPage import LoginPage
from pageObjects.ModifyProductPage import ModifyProduct
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from selenium import webdriver

class Test_004_ModifyProduct:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen() #logger

    @pytest.mark.regression
    def test_ModifyProductPrice(self, setup):
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

        self.logger.info("*************** Starting Add Customer Test ***************")
        self.product = ModifyProduct(self.driver)
        self.product.clickCatalogMenu()
        self.product.clickProductsMenuItem()

        time.sleep(3)
        self.noOfPages = self.product.getNoOfNavPages()

        self.validationPt = False
        for i in range(int(self.noOfPages)):
            count = 0
            time.sleep(3)
            self.allProductsName = self.driver.find_elements(By.XPATH, "//tbody//tr//td[3]")
            for j in self.allProductsName:
                count += 1
                if j.text == "$100 Physical Gift Card":
                    self.logger.info("*************** Element found, Clicking on edit ***************")
                    self.product.clickEdit(count)
                    self.validationPt = True
                    time.sleep(7)
                    assert True

            if self.validationPt == False:
                self.product.clickRightNav()
        print("Trying to print here")
        self.driver.find_element(By.XPATH, "//input[@id='AvailableEndDateTimeUtc']").clear()
        self.driver.find_element(By.XPATH, "//button[@name='save']").click()

        self.driver.close()


