import unittest
from Module.BrandManagement import BrandManagementMod
from generic.path import *
from StumpLogging import Customlogger as cl
import logging
import pytest,time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp", "folder")
class testBM (unittest.TestCase):
    # log = cl.customLogger(logging.DEBUG)
    log = cl.customLogger('false', logging.DEBUG)
    log.info("-------------------------------START--------------------------------------")
    log1 = cl.customLogger('true', logging.DEBUG)

    @pytest.fixture(autouse=True)
    def setup(self):
        self.bm = BrandManagementMod(self)

    @pytest.mark.run()
    def test(self):
        self.bm = BrandManagementMod(self.driver)
        self.bm.menu_bar_test()
        self.bm.go_to_module()
        self.bm.text_enter_test()
        self.bm.test_filter()
        # self.bm.filter_days_check()
        # self.bm.test_delete()
        # self.bm.test_edit()
        # self.bm.test_addlocation()
        # self.bm.fill_manually_test()
        # self.bm.next_page_list
        # self.bm.test_location_present()
        # self.bm.test_map_view()