from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        service_obj = Service("C:\Automation Testing Drivers\chromedriver_win32\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        print("Launching Chrome browser")
    elif browser == "firefox":
        service_obj = Service("C:\Automation Testing Drivers\geckodriver-v0.30.0-win64\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
        print("Launching Firefox browser")
    else:
        service_obj = Service("C:\Automation Testing Drivers\edgedriver_win64\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
        print("Launching Edge browser")
    return driver

def pytest_addoption(parser):  #This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):   #This will return the browser value to setup method
    return request.config.getoption("--browser")

########## Pytest HTML Repost ##########

def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Akshay'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)



