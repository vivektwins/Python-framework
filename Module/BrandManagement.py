from generic import base_page
from generic.base_page import BasePage
from generic.locators import Locators
import time



class BrandManagementMod(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    Menu_bar = 'dropdown'
    Location_page ="//*[text()='Location Management']"
    Map_Text = "map-form"
    Map_autofill = "rbt-input"
    Map_name_dropdown = "select-control"
    Apply = "go-bttn"
    Edit = "edit-img"
    Delete = "delete-img"
    Address_edit = "address" #id
    City_edit = "city" #id
    State_edit = "state" # id
    pincode_edit = "pinCode" #id
    name_edit = "name" #id
    Days_box = '//*[contains(@id,"8")]//input'
    Save_button = "map-save-button"
    Back_button = "back-bttn-custom"
    Delete_popup_no = "btn-mod-left"
    Delete_popup_yes = "btn-mod-right"
    Show_map_view = "show-map-view"
    Next_button = "//*[@id='root']/div/div[1]/div[2]/div/div[1]/div[1]/div[4]/ul/li[5]/a"
    Add_Location = "right-button"
    Manually_Address = "//button[text()='Add address manually']"
    manual_popup_cancel = "modal-footer-border"
    Location_name_list ="loc-data"
    Filter_name_days = 'select-control'
    Remove_filter_click = 'on-remove'
    Location_page_title = 'app-header-title'
    Next_page_list = 'navbar-nav-sm'
    All_locations = '[role="menu"] span div div div'
    Link_Data_Reporting = "//*[text()='Data Reporting']"
    Locations_drop_down = '[style="color: rgba(0, 0, 0, 0.87); height: 56px; line-height: 56px; overflow: hidden; opacity: 1; position: relative; padding-left: 0px; padding-right: 56px; text-overflow: ellipsis; top: 6px; white-space: nowrap;"]'


    def menu_bar_test(self):

        """Clicking the Menu bar"""

        self.elementClick(self.Menu_bar, locatorType='class')
        time.sleep(5)


    def go_to_module(self):
        
        """"Clicking the locationManagement Link from Menu bar"""

        self.elementClick(self.Location_page, locatorType='xpath')


    def text_enter_test(self):
        
        """sending the text in google map input box"""

        self.dropdown_click_option(self.Map_Text, "andaman and nicobar islands", type='class', locname='pac-item')
        time.sleep(2)


    def test_filter(self):
        
        """sending the text in Location name  input box and filter is working or not"""

        self.dropdown_click_option(self.Map_autofill, "hashedin", type='class', locname='dropdown-item')
        time.sleep(5)
        self.elementClick(self.Apply, locatorType='class')
        time.sleep(5)
        self.elementClick(self.Remove_filter_click, locatorType='class')
        self.elementClick(self.Apply, locatorType='class')


    def filter_days_check(self):
        
        """Clicking filter Name/Days Filter option"""

        self.dropdown(self.Filter_name_days, "Days", type='class', locname='select-control')


    def test_delete(self):

        """Test the delete button is working or not"""

        time.sleep(3)
        self.elementClick(self.Delete, locatorType='class')
        self.elementClick(self.Delete_popup_no, locatorType='class')
        text = self.getText(self.Location_page_title, locatorType='class')
        final = str(text.lower())
        if 'location management' == final:
            self.log.info("Delete popup No - Verification Pass")
        else:
            self.log.info("Delete popup No - Verification Fail")
    

    def test_edit(self):

        """To ensure edit Button is working or not"""

        time.sleep(3)
        self.elementClick(self.Edit, locatorType='class')
        self.elementClick(self.Back_button, locatorType='class')
        time.sleep(3)
        text = self.getText(self.Location_page_title, locatorType='class')
        final = str(text.lower())
        if 'location management' == final:
            self.log.info("Edit and back case - Verification Pass")
        else:
            self.log.info("Edit and back case - Verification Fail")
        time.sleep(3)


    def test_addlocation(self):

        """Clicking the AddLocation and adding the location manually"""

        self.elementClick(self.Add_Location, locatorType='class')
        self.sendKeys(data='testLocationName', locator=self.name_edit, locatorType='id')
        self.elementClick(self.Days_box, locatorType='xpath')
        self.elementClick(self.Save_button, locatorType='class')
        self.elementClick(self.Manually_Address, locatorType='xpath')


    def fill_manually_test(self):

        """Filling the data manually"""

        time.sleep(3)
        self.sendKeys(data='Add', locator=self.Address_edit, locatorType='id')
        self.sendKeys(data='city', locator=self.City_edit, locatorType='id')
        self.sendKeys(data='Kar', locator=self.State_edit, locatorType='id')
        self.sendKeys(data='4544544', locator=self.pincode_edit, locatorType='id')
        self.elementClick(self.Save_button, locatorType='class')
    

    def nextpage_check(self):

        """Iterating the Next page and selecting the last page"""

        time.sleep(3)
        # self.elementClick(self.Menu_bar, locatorType='class')
        # self.elementClick(self.Location_page, locatorType='xpath')
        dat = (self.getElementList(self.Next_page_list, locatorType='class'))
        list1 = str(dat)
        for i in list1:
            self.elementClick(self.Next_button, locatorType='xpath')
            if 'disabled' in i:
                break
    

    def test_location_present(self):

        """Checking if location is created or not"""

        time.sleep(2)
        self.elementClick(self.Menu_bar, locatorType='class')
        self.elementClick(self.Link_Data_Reporting, locatorType='xpath')
        self.elementClick(self.Locations_drop_down, locatorType='css')
        List = self.getElementList(locator=self.All_locations, locatorType='css')
        time.sleep(5)
        # time.sleep(5)
        self.log.info(List)
        for loc in List:
            try:
                IterateData = str(loc.text.lower())
                # self.log.info(IterateData)
                if 'testlocationname' == IterateData:
                    self.log.info("Location is created")
                    break
                # else:
                #     #self.log.info('location is not created')
            except:
                self.log.info("Data is not available")
        

    def test_map_view(self):

        """Checking the show Map view"""

        time.sleep(2)
        self.elementClick(self.Add_Location, locatorType='class')
        self.elementClick(self.Save_button, locatorType='class')
        self.elementClick(self.Manually_Address, locatorType='xpath')
        time.sleep(3)
        self.elementClick(self.Show_map_view, locatorType='class')
        self.elementClick(self.Back_button, locatorType='class')
        time.sleep(3)
    

