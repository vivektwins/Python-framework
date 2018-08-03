import pytest
from generic.Webdriver_factory import WebDriverFactory
from generic.path import *
from generic.locators import Locators
import os
from datetime import date
from datetime import datetime
import time

hostlogin = 'login-host'
email = 'email'  # id
password = 'password'  # id
submit = 'btn-success'
back = 'login-back-button'
Team_Name = 'teamname'
Play_game = 'quicksand-bold'

driver =0


@pytest.yield_fixture()
def setUp():
    print("Running setUp for test case")
    yield
    print("Running tearDown for test case")


@pytest.yield_fixture()
def oneTimeSetUp(request, browser):
    global driver
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()

    #print(" Running one time tearDown")

@pytest.yield_fixture()
def login():
    global driver
    lc = Locators(driver)
    lc.elementClick(hostlogin, locatorType="class")
    lc.sendKeys(data='vivekkumam26@gmail.com', locator=email, locatorType="id")
    lc.sendKeys(data='!321Shoot', locator= password, locatorType="id")
    lc.elementClick(submit,locatorType="class")
    time.sleep(2)


# @pytest.yield_fixture(scope="class")
# def players_setup(request,browser):
#
#         print("Running one time setUp")
#         wdf = WebDriverFactory(browser)
#         driver = wdf.getWebDriverInstance()
#         time.sleep(2)
#         lc = Locators(driver)
#         lc.elementClick(Play_game,locatorType='class')
#         lc.sendKeys(data = ' ', locator=Team_Name,locatorType= 'id')
#
#
#         if request.cls is not None:
#             request.cls.driver = driver
#         yield driver
#         driver.quit()
#         # print(" Running one time tearDown")


def pytest_addoption(parser):
      parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.yield_fixture()
def folder():
    today = date.today()
    print(today)
    time = datetime.now()
    print(time)

    file_path = ".\\StumpNew"
    # directory = os.path.dirname(file_path)
    try:
        print(os.getcwd())
        if not os.path.exists(file_path):
            os.chdir("C:\\Users\\Hasher\\PycharmProjects\\StumpNew")
            print("pass")
            os.mkdir(str(today))
            print(os.getcwd())
        else:
            print("path is already created")

    except OSError:
        print('Error: Creating directory. ' + file_path)


