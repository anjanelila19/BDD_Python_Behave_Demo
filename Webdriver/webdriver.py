from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def get_webdriver(webdriver_type):
    if webdriver_type == "edge":
        driver = webdriver.Edge()
    elif webdriver_type == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome(service=Service("C:\\Users\\A200167704\\Downloads\\SELENIUM_BEHAVE_FRAMEWORK-master\\SELENIUM_BEHAVE_FRAMEWORK-master\\Webdriver\\chromedriver.exe"))
    return driver