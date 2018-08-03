from generic import base_page
from generic.base_page import BasePage
from generic.locators import Locators
import time


class DataMod (BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    Menu_bar = 'dropdown'
    Link_Data_Reporting = "//*[text()='Data Reporting']"
    Start_date = 'StartDatePicker'
    End_date = 'EndDatePicker'
    calendar_end = "/html/body/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div[3]/div/div/div[4]/button[6]"
    calendar_cancel = "//*[text()='Cancel']"
    Go_button = "//*[text()='GO']"
    Locations_drop_down = '[style="color: rgba(0, 0, 0, 0.87); height: 56px; line-height: 56px; overflow: hidden; opacity: 1; position: relative; padding-left: 0px; padding-right: 56px; text-overflow: ellipsis; top: 6px; white-space: nowrap;"]'
    Button_click = '//*[@id="root"]/div/div[1]/div[2]/div/div/div/div/div/div/div[3]/div/div/div[1]/table/tbody/tr[4]/td[3]/img'
    Disable_Button_click = '//*[@id="root"]/div/div[1]/div[2]/div/div/div/div/div/div/div[3]/div/div/div[1]/table/tbody/tr[5]/td[3]/img'
    Next_button = "(//a[@[role='button'])[last()]"
    previous_button = '//*[@id="root"]/div/div[1]/div[2]/div/div/div/div/div/div/div[3]/div/div/div[2]/ul/li[1]/a'
    Host_up_button = ''
    Host_down_button = '.first-pending-th .down'
    No_of_games_up = '//*[@id="root"]/div/div[1]/div[2]/div/div/div/div/div/div/div[3]/div/div/div[1]/table/thead/tr/th[2]/span/i[1]'
    No_of_games_down = '.undefined .down'
    All_locations = '[role="menu"] span div div div'
    Question_set_click = '//*[@id="root"]/div/div[1]/div[2]/div/div/div/div/div/div/div[3]/div/div[2]/div/div/div[1]/table/tbody/tr[1]/td[3]/span/div/div/span/a'
    PreviewPopup_exit = 'preview-footer-button-full'
    Host_click = 'abled-row'
    Disabled_calendar = '[disabled]:nth-of-type(3)'
    Next_page_list = 'navbar-nav-sm'
    
    
    
    def menu_bar_test(self):
    
        """Clicking the Menu bar"""

        self.elementClick(self.Menu_bar, locatorType='class')
        time.sleep(5)

    def go_to_module(self):

        """clicking to module page"""

        self.elementClick(self.Link_Data_Reporting,locatorType='xpath')

    def selecting_date_range(self):

        """Selecting the date"""
    
        self.elementClick(self.Start_date, locatorType='id')
        self.elementClick(self.calendar_cancel,locatorType='xpath')

    def selecing_disabled_date(self):
    
        """Selecting the today's date and ensure the Disabled date is clicked or not"""
    
    
        time.sleep(3)
        self.elementClick(self.End_date, locatorType='id')
        self.elementClick(self.Disabled_calendar,locatorType='css')
        time.sleep(3)
        self.elementClick(self.calendar_cancel, locatorType='xpath')
        time.sleep(3)
        self.elementClick(self.Go_button, locatorType='class')

    def selecting_location(self):

        """clicking the locations"""

        time.sleep(3)
        self.dropdown(self.Locations_drop_down, "Demonewnew", type='css', locname='[role="menu"] span div div div')

    def button_click_check(self):

        """clicking the buttons"""

        time.sleep(3)
        self.elementClick(self.Button_click,locatorType='xpath')
        self.elementClick(self.Question_set_click,locatorType='xpath')
        self.elementClick(self.PreviewPopup_exit,locatorType='class')
        time.sleep(3)
        self.elementClick(self.Host_click,locatorType='class')



    def filters_check(self):


        time.sleep(3)
        self.elementClick(self.Host_down_button,locatorType='css')
        self.elementClick(self.No_of_games_down, locatorType='css')

        """Iterating the Next page and selecting the last page"""

        time.sleep(3)
        # self.bm.elementClick(self.bm.Menu_bar, locatorType='class')
        # self.bm.elementClick(self.bm.Location_page, locatorType='xpath')
        dat = (self.getElementList(self.Next_page_list, locatorType='class'))
        list1 = str(dat)
        for i in list1:
            self.elementClick(self.Next_button, locatorType='xpath')
            if 'disabled' in i:
                break
