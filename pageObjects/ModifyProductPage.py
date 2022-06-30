from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ModifyProduct:
    lnk_Catalog_xpath = "//p[normalize-space()='Catalog']//i[contains(@class,'right fas fa-angle-left')]"
    lnk_ProductsMenuItem_xpath = "//p[normalize-space()='Products']"
    btn_RightNav_xpath = "//li[@id='products-grid_next']//a[@class='page-link']"
    lnk_Pagination_xpath = "//ul[@class='pagination']//li//a"
    # btn_Edit_xpath = f"//tbody//tr[{x}]//td[@class=' button-column']//a"

    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()

    def clickCatalogMenu(self):
        self.driver.find_element(By.XPATH, self.lnk_Catalog_xpath).click()

    def clickProductsMenuItem(self):
        self.Explicit_wait = WebDriverWait(self.driver, 10, poll_frequency=2, ignored_exceptions=[Exception])
        self.Explicit_wait.until(EC.element_to_be_clickable((By.XPATH, self.lnk_ProductsMenuItem_xpath)))
        self.driver.find_element(By.XPATH, self.lnk_ProductsMenuItem_xpath).click()

    def getNoOfNavPages(self):
        self.nav = self.driver.find_elements(By.XPATH, self.lnk_Pagination_xpath)
        self.noOfPages = self.nav[-2].text
        return self.noOfPages

    def clickRightNav(self):
        self.driver.find_element(By.XPATH, self.btn_RightNav_xpath).click()

    def clickEdit(self, value):
        self.btn_Edit_xpath = f"//tbody//tr[{value}]//td[@class=' button-column']//a"
        self.driver.find_element(By.XPATH, self.btn_Edit_xpath).click()

