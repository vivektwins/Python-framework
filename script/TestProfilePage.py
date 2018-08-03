import unittest
from Module.Profile import ProfileMod
from generic.path import *
from StumpLogging import Customlogger as cl
import logging
import pytest, time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp", "folder")
class testPM (unittest.TestCase):
    # log = cl.customLogger(logging.DEBUG)

    log = cl.customLogger('false', logging.DEBUG)
    log.info("-------------------------------START--------------------------------------")
    log1 = cl.customLogger('true', logging.DEBUG)


    @pytest.fixture(autouse=True)
    def setup(self):
        self.pm = ProfileMod(self)

    @pytest.mark.run()
    def test(self):
        self.pm = ProfileMod(self.driver)
        self.pm.menu_bar_test()
        self.pm.valid_case()
        self.pm.invalid_case()
        self.pm.white_space_test()
        self.pm.mandatory_check()
        self.pm.more_numbers()
        self.pm.no_popup()
        self.pm.change_pass_check()
        self.pm.yes_popup()
        self.pm.log_out()
