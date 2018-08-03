from selenium import webdriver
from generic.path import *


class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        if self.browser == "firefox":
            driver = webdriver.Firefox(executable_path=FF_DRIVER_PATH)
        elif self.browser == "chrome":
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        else:
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        driver.implicitly_wait(IMPLICITLY_WAIT)
        driver.maximize_window()
        driver.get(BASE_URL)
        return driver