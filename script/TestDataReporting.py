import unittest
from Module.DataReporting import DataMod
from generic.path import *
from StumpLogging import Customlogger as cl
import logging
import pytest, time


@pytest.mark.usefixtures("oneTimeSetUp", "login", "folder")
class testDR (unittest.TestCase):
    # log = cl.customLogger(logging.DEBUG)
    log = cl.customLogger('false', logging.DEBUG)
    log.info("-------------------------------START--------------------------------------")
    log1 = cl.customLogger('true', logging.DEBUG)


    @pytest.fixture(autouse=True)
    def setup(self):
        self.dm = DataMod(self)

    def test(self):
        self.dm = DataMod(self.driver)
        self.dm.menu_bar_test()
        self.dm.go_to_module()
        self.dm.selecting_date_range()
        self.dm.selecing_disabled_date()
        self.dm.selecting_location()
        self.dm.button_click_check()
        self.dm.Filters_check()
