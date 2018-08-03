from generic import base_page
from generic.base_page import BasePage
from generic.locators import Locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time


class AccountMStump(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    Menu_bar = 'dropdown'
    Account_Management_sub = 'dashboard-link'
    Active = '[aria-controls="Active"]' #css
    Deactivated = '[aria-controls="Deactivated"]' #CSS
    Wait = '[aria-controls="Wait"]'
    NextPage = '' #li
    accept = "//img[@alt='accept']"
    reject_pending = "//img[@alt='remove']"
    reject_reason = "//textarea[@placeholder='Description']"
    reject_reason_submit = "//span[text()='Submit']"

    #Activate Tab
    deactivatelink = 'host-btn'
    PopupRejection = 'login-form-field'
    cancelpopup = 'btn-mod-left'
    SubmitPopup = 'btn-mod-right'


    def menu(self):

        """ clicking the menu bar """

        self.elementClick(self.Menu_bar, locatorType='class')
        time.sleep(2)

    def acc(self):

        """Selecting the required module"""

        self.elementClick(self.Account_Management_sub,locatorType='class')
        time.sleep(2)

    def active(self):

        """ Selecting the active tab"""

        self.tab_click(self.Active, locatorType='CSS')
        time.sleep(2)


    def deact(self):

        """Selecting the deactive tab"""

        self.tab_click(self.Deactivated,locatorType='CSS')

    def wait(self):

        """Selecting the wait tab"""

        self.tab_click(self.Wait, locatorType='CSS')
        time.sleep(2)

    def next_button(self):

        """Selecting the next_button"""

        self.elementClick(self.NextPage,locatorType='')
        for i in next:
            if i == 'active':
                self.elementClick()
            else :
                break
