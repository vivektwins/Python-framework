from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.alert import Alert
from traceback import print_stack
from StumpLogging import Customlogger as cl
import logging
import os
import time


class Locators():


    """
    Class which works as a custom selenium driver for using few custom generic methods
    """

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def getTitle(self):
        return self.driver.title

    def getElement(self, locator, locatorType =""):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator: " + locator + " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator + " and  locatorType: " + locatorType)
        return element

    def tab_click(self, locator, locatorType=""):
        try:
            locatorType = locatorType.lower()
            self.elementClick(locator, locatorType)
            self.log.info("Element Found with locator: " + locator + " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator + " and  locatorType: " + locatorType)

    def dropdown_click_option(self,dropdown, data, type, locname):
        try:
            select = self.getElement(locator=dropdown, locatorType=type)
            self.sendKeys(data, dropdown, type)
            time.sleep(10)

            if type == 'class':
                multiple = self.driver.find_elements_by_class_name(locname)

            elif type == 'xpath':
                multiple = self.driver.find_elements_by_xpath(locname)

            elif type == 'css':
                multiple = self.driver.find_elements_by_css_selector(locname)

            for option in multiple:
                try:
                    IterateData = str(option.text.lower())
                    self.log.info(IterateData)
                    if str(data.lower()) == IterateData:
                        self.log.info(option.text + "\t" + "test" + "\t" + data)
                        time.sleep(10)
                        self.log.info(option.click)
                        option.click()
                        self.log.info("Element clicked" + option)
                        break

                except:
                    self.log.info("Element with text not found in the drop down" + option)
        except:
            self.log.info("Drop down not found with the given path")


    def dropdown(self, dropdown, data, type, locname):
        try:
            select = self.getElement(locator=dropdown, locatorType=type)
            self.elementClick(locator=dropdown, locatorType=type)
            time.sleep(10)
            self.log.info("pass0" + type)
            #self.log.info(list)

            if type == 'class':
                multiple = self.driver.find_elements_by_class_name(locname)

            elif type == 'xpath':
                multiple = self.driver.find_elements_by_xpath(locname)

            elif type == 'css':
                multiple = self.driver.find_elements_by_css_selector(locname)

            for option in multiple:
                try:
                    IterateData = str(option.text.lower())
                    self.log.info(IterateData)
                    if str(data.lower()) == IterateData:
                        self.log.info(option.text + "\t" + "test" + "\t" + data)
                        time.sleep(10)
                        self.log.info(option.click)
                        option.click()
                        self.log.info("Element clicked" + option)
                        break

                except:
                    self.log.info("Element with text not found in the drop down")
        except:
            self.log.info("Drop down not found with the given path")

    def getElementList(self, locator, locatorType=""):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.info("Element list not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element


    def webScroll(self, direction="up"):
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 50);")


    def elementClick(self, locator="", locatorType="", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator, locatorType="", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)
            print_stack()
            return element

    def clearText(self, locator="", locatorType="", element=None):
        try:
            if locator:
                self.getElement(locator, locatorType).clear()
            element.clear()
            self.log.info("Cleared content from the field with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot clear content from the field with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def getText(self, locator="", locatorType="", element=None, info=""):
        """
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                #text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def getElementListText(self, locator="", locatorType=""):
        elements_list = self.getElementList(locator=locator, locatorType=locatorType)
        list_text = []
        for items in elements_list:
            list_text.append(self.getText(element=items))
        return list_text


    def isElementPresent(self, locator="", locatorType="", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def isElementDisplayed(self, locator="", locatorType="", element=None):
        """
        NEW METHOD
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            else:
                self.log.info("Element not displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            return isDisplayed
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self, locator, locatorType="",
                               timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                              "stopFilter_stops-0")))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def unique_value_from_list(self, all_values):
        unique_words = []
        for i in all_values:
            if not i in unique_words:
                unique_words.append(i)
        return unique_words

    def plusClick(self, locator="",locatorType=""):

        try:
            if locator:
                self.elementClick(locator , locatorType)
                time.sleep(5)
                self.log.info("First plus element found: " + locator +
                          " locatorType: " + locatorType)
            if locator:
                self.elementClick(locator , locatorType)
                time.sleep(5)
                self.log.info("second plus element found: " + locator + "locator: " +  locatorType)

            if locator:
                self.elementClick(locator,locatorType)
                time.sleep(5)
                self.log.info("Third plus element found: " + locator + "locator: " +  locatorType)

            else:
                self.log.info("No plus click found:")

        except:
                self.log.info("No plus click found:")

    def isElementSelected(self,locator, locatorType="", element=None):

        isSelected = False
        try:
            if locator:
                element = self.getElement(locator,locatorType)

            if element is not None:
                isSelected = element.is_selected()
                self.log.info("Element is selected with locator: " + locator +
                              " locatorType: " + locatorType)
            else:
                self.log.info("Element not selected with locator: " + locator +
                              " locatorType: " + locatorType)
            return isSelected
        except:
            print("Element not found")
            return False



    def check_box(self,locator,locatorType=""):
        try:
            if locator:
                locatorType = locatorType.lower()
                self.elementClick(locator ,locatorType)
                self.isElementSelected()
            else:
                self.log.info("Clicked on check box element with locator: " + locator + " locatorType: " + locatorType)
        except:
                self.log.info("Cannot click on the checkbox element with locator: " + locator + " locatorType: " + locatorType)
                print_stack()


    def screenShot(self, resultMessage):
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshot/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot saved to directory : " + destinationFile)
        except:
            self.log.error("### EXCEPTION OCCURRED")
            print_stack()

