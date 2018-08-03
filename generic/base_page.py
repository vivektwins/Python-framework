from generic.locators import Locators
from traceback import print_stack

class BasePage(Locators):

    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.driver = driver


    def verifyPageTitle(self, titleToVerify):
        """
        Verify the page_folder Title

        Parameters:
            titleToVerify: Title on the page_folder that needs to be verified
        """
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page_folder title")
            print_stack()
            return False



    def verifyTextContains(self, actualText, expectedText):
        """
        Verify actual text contains expected text string

        Parameters:
            expectedList: Expected Text
            actualList: Actual Text
        """
        self.log.info("Actual Text From Application Web UI --> :: " + actualText)
        self.log.info("Expected Text From Application Web UI --> :: " + expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("### VERIFICATION CONTAINS !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT CONTAINS !!!")
            return False
