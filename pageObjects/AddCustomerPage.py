import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    # Add customer page
    lnk_CustomerMenu_xpath = "//p[normalize-space()='Customers']//i[contains(@class,'right fas fa-angle-left')]"
    lnk_CustomerMenuItem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btn_AddNew_xpath = "//a[@class='btn btn-primary']"
    txt_Email_xpath = "//input[@id='Email']"
    txt_Password_xpath = "//input[@id='Password']"
    txt_FirstName_xpath = "//input[@id='FirstName']"
    txt_LastName_xpath = "//input[@id='LastName']"
    rd_Male_xpath = "//input[@id='Gender_Male']"
    rd_Female_xpath = "//input[@id='Gender_Female']"
    txt_DOB_xpath = "//input[@id='DateOfBirth']"
    txt_CompanyName_xpath = "//input[@id='Company']"
    txt_CustomerRoles_xpath = "//div[@class='input-group-append input-group-required']//input[@role='listbox']"
    lstitem_Administrators_xpath = "//li[normalize-space()='Administrators']"
    lstitem_ForumModerators_xpath = "//li[normalize-space()='Forum Moderators']"
    lstitem_Guest_xpath = "//li[normalize-space()='Guests']"
    lstitem_Registered_xpath = "//li[normalize-space()='Registered']"
    lstitem_Vendors_xpath = "//li[contains(text(),'Vendors')]"
    lst_ManagerOfVendor_xpath = "//select[@id='VendorId']"
    txt_AdminComment_xpath = "//textarea[@id='AdminComment']"
    btn_Save_xpath = "//button[@name='save']"


    def __init__(self, driver):
        self.driver = driver


    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.lnk_CustomerMenu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnk_CustomerMenuItem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.btn_AddNew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txt_Email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txt_Password_xpath).send_keys(password)

    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH, self.txt_FirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txt_LastName_xpath).send_keys(lname)

    def setGender(self, gender):
        if gender == "male":
            self.driver.find_element(By.XPATH, self.rd_Male_xpath).click()
        elif gender == "female":
            self.driver.find_element(By.XPATH, self.rd_Female_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rd_Male_xpath).click()

    def setDOB(self, dob):
        self.driver.find_element(By.XPATH, self.txt_DOB_xpath).send_keys(dob)

    def setCompanyName(self, companyName):
        self.driver.find_element(By.XPATH, self.txt_CompanyName_xpath).send_keys(companyName)

    def setCustomerRoles(self, customerRoles):
        self.driver.find_element(By.XPATH, self.txt_CustomerRoles_xpath).click()
        time.sleep(3)
        if customerRoles == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_Registered_xpath)
        elif customerRoles == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_Administrators_xpath)
        elif customerRoles == "Forum Moderators":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_ForumModerators_xpath)
        elif customerRoles == "Guests":
            self.driver.find_element(By.XPATH, "//span[@title='delete']").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_Guest_xpath)
        elif customerRoles == "Vendors":
            self.driver.find_element(By.XPATH, self.lstitem_Vendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_Registered_xpath)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, vendor):
        drpdown = Select(self.driver.find_element(By.XPATH, self.lst_ManagerOfVendor_xpath))
        drpdown.select_by_visible_text(vendor)

    def setAdminComment(self, comment):
        self.driver.find_element(By.XPATH, self.txt_AdminComment_xpath).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btn_Save_xpath).click()












