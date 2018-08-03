import unittest
from Module.AccountManagement import AccountMStump
from generic.path import *
from StumpLogging import Customlogger as cl
import logging
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "login", "folder")
class testacc (unittest.TestCase):
    # log = cl.customLogger(logging.DEBUG)
    log = cl.customLogger('false', logging.DEBUG)
    log.info("-------------------------------START--------------------------------------")
    log1 = cl.customLogger('true', logging.DEBUG)

    @pytest.fixture(autouse=True)
    def setup(self):
        self.st = AccountMStump(self)

    @pytest.mark.run(order=1)
    def test_methods(self):
        self.st = AccountMStump(self.driver)
        self.st.menu()
        self.st.acc()
        self.st.active()
        self.st.deact()
        self.st.wait()
