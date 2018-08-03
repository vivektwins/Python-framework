from generic import base_page
from generic.base_page import BasePage
from generic.locators import Locators
import time

class ProfileMod(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    Menu_bar = 'dropdown'
    Profilelink = "//a[text()='Profile']"
    Username = 'username' #id
    firstname = 'firstName' #id
    Lastname = 'lastName' #id
    Phno = 'phoneNumber'
    SaveButton = 'bttn-green'
    BackButton = 'back-bttn-custom'
    NoPopup = 'btn-mod-left'
    YesPopup = 'btn-mod-right'
    changePassword = 'loginError' #id
    oldPassWord = 'oldPasswordText' #id
    NewPassWord = 'newPasswordText1' #id
    ReconfirmNewPw = 'newPasswordText2' #id
    Password_Reveal = 'password-reveal-btn'
    Error_Msg = "//*[text()='Your no. should be only digits and the length should not exceed 16.']"
    Location_page = "//*[text()='Location Management']"
    Profile_Title = 'app-header-title'
    Mandatory = "//*[text()='Fields marked with an * are mandatory']"
    Log_out = "//*[text()= 'Logout']"

    def clear(self):

        """ Clearing the text fields """

        self.clearText(locator=self.firstname, locatorType='id')
        self.clearText(locator=self.Lastname, locatorType='id')
        self.clearText(locator=self.Phno, locatorType='id')

    
    def menu_bar_test(self):

        """Landing into Profile Page"""
    
        self.elementClick(self.Menu_bar, locatorType='class')
        time.sleep(3)
        self.elementClick(self.Profilelink, locatorType='xpath')

    def valid_case(self):

        """Valid case with filling the data"""
        
        #self.clear()
        # #self.clearText(locator=self.firstname, locatorType='id')
        # #self.clearText(locator=self.Lastname, locatorType='id')
        # #self.clearText(locator=self.Phno, locatorType='id')
        # time.sleep(3)
        # self.sendKeys(data= 'vk',locator=self.firstname, locatorType= 'id')
        # self.sendKeys(data='kumar', locator=self.Lastname, locatorType='id')
        # self.sendKeys(data='12', locator=self.Phno, locatorType='id')
        # self.elementClick(self.SaveButton,locatorType='class')
        # time.sleep(3)
        # text = self.getText(locator=self.Error_Msg, locatorType='xpath')
        # if 'Your no. should be only digits and the length should not exceed 16.' != text:
        #     self.log.info("Valid case - Verification pass")
        # else:
        #     self.log.info("Valid case - Verification fail")
        # time.sleep(3)

    
    def invalid_case(self):

        """With Invalid case"""
    
        self.clear()
        time.sleep(3)
        self.sendKeys(data='ffhgg', locator=self.firstname, locatorType='id')
        self.sendKeys(data='hgffhg', locator=self.Lastname, locatorType='id')
        self.sendKeys(data='invalid', locator=self.Phno, locatorType='id')
        self.elementClick(self.SaveButton, locatorType='class')
        time.sleep(3)
        text = self.getText(locator=self.Error_Msg, locatorType='xpath')
        if 'Your no. should be only digits and the length should not exceed 16.' in text:
            self.log.info("InValid case - Verification pass")
        else:
            self.log.info("InValid case - Verification fail")
        time.sleep(3)

    
    def white_space_test(self):

        """White space in Phone number check"""
    
        self.clearText(locator=self.Phno, locatorType='id')
        time.sleep(3)
        self.sendKeys(data=' ', locator=self.Phno, locatorType='id')
        self.elementClick(self.SaveButton, locatorType='class')
        time.sleep(3)
        text = self.getText(locator=self.Error_Msg, locatorType='xpath')
        if 'Your no. should be only digits and the length should not exceed 16.' in text:
            self.log.info("White space case - Verification pass")
        else:
            self.log.info("White space case - Verification fail")
        time.sleep(3)

    def mandatory_check(self):

        """Test to submit without filling the mandatory fields"""

        self.clear()
        time.sleep(10)
        # self.sendKeys(data='123 ', locator=self.Phno, locatorType='id')
        # self.clear()
        # time.sleep(3)
        self.elementClick(self.SaveButton, locatorType='class')
        time.sleep(3)
        text = self.getText(locator=self.Mandatory, locatorType='xpath')
        self.log.info(text, "Error case")
        if 'Your no. should be only digits and the length should not exceed 16.' != text:
            self.log.info("Required field case - Verification pass")
        else:
            self.log.info("Required field case - Verification fail")
        time.sleep(3)

    def more_numbers(self):

        """With more than 16 numbers in Mobile phone"""
    
        self.clearText(locator=self.Phno, locatorType='id')
        time.sleep(3)
        self.sendKeys(data='12345678910121314516 ', locator=self.Phno, locatorType='id')
        self.elementClick(self.SaveButton, locatorType='class')
        time.sleep(3)
        text = self.getText(locator=self.Error_Msg, locatorType='xpath')
        if 'Your no. should be only digits and the length should not exceed 16.' in text:
            self.log.info("With More number case - Verification pass")
        else:
            self.log.info("With More number case - Verification fail")
        time.sleep(3)

    def no_popup(self):

        """check the popup case with No option"""
    
        self.elementClick(self.Menu_bar, locatorType='class')
        self.elementClick(self.Location_page, locatorType='xpath')
        time.sleep(3)
        self.elementClick(self.NoPopup, locatorType='class')
        time.sleep(3)
        text = self.getText(self.Profile_Title, locatorType='class')
        if 'profile details' == str(text.lower()):
            self.log.info("Popup No case - Verification Pass")
        else:
            self.log.info("Popup No case - Verification Fail")
        time.sleep(3)

    def change_pass_check(self):

        """To check change password is working or not"""
        
        self.elementClick(self.changePassword, locatorType='id')
        self.sendKeys(data='sddsf', locator=self.oldPassWord, locatorType='id')
        self.elementClick(self.Password_Reveal, locatorType='class')
        self.elementClick(self.BackButton, locatorType='class')
        time.sleep(3)

    def yes_popup(self):

        """check the popup case with Yes option"""
    
        self.elementClick(self.Menu_bar, locatorType='class')
        self.elementClick(self.Location_page, locatorType='xpath')
        time.sleep(3)
        self.elementClick(self.YesPopup, locatorType='class')
        text = self.getText(self.Profile_Title, locatorType='class')
        if 'Profile Details' not in text:
            self.log.info("Popup Yes case - Verification Pass")
        else:
            self.log.info("Popup Yes case - Verification Fail")

    def log_out(self):

        """Logging out"""
    
        time.sleep(3)
        self.elementClick(self.Menu_bar, locatorType='class')
        self.elementClick(self.Log_out, locatorType='xpath')
