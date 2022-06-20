import random
import string
import pytest
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from selenium import webdriver

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen() #logger

    @pytest.mark.regression
    def test_addCustomer(self, setup):
        self.logger.info("*************** Test_003_AddCustomer ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*************** Login Successful ***************")

        self.logger.info("*************** Starting Add Customer Test ***************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.addcust.clickOnAddNew()

        self.logger.info("*************** Providing Customer Information ***************")
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Akshay Pratap")
        self.addcust.setLastName("Singh")
        self.addcust.setGender("male")
        self.addcust.setDOB("1/12/1998")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 1")
        self.addcust.clickOnSave()

        self.logger.info("*************** Saving Customer Information ***************")

        self.msg = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissable']").text
        if "customer has been added successfully" in self.msg:
            assert True
            self.logger.info("*************** Add Customer Test Passed ***************")
        else:
            self.driver.save_screenshot("C:\\Users\\Akshay\\PycharmProjects\\SeleniumHybridFramework\\Screenshots"+"\\test_addCustomer.png")
            self.logger.error("*************** Add Customer Test Failed ***************")
            assert False

        self.driver.close()
        self.logger.info("*************** Ending Home Page Title Test ***************")


def random_generator(size=8, chars=string.ascii_lowercase +string.digits):
    return ''.join(random.choice(chars) for x in range(size))












