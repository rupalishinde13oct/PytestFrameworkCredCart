import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')

@pytest.fixture()
def setup(browser):

    if browser == 'chrome':
        d = webdriver.Chrome()

    elif browser == 'firefox':
        d = webdriver.Firefox()

    elif browser == 'edge':
        d = webdriver.Edge()

    else:
        # opt = webdriver.ChromeOptions()
        # opt.add_argument("headless")
        # d = webdriver.Chrome(options=opt)
        d = webdriver.Chrome()

    d.maximize_window()
    d.implicitly_wait(10)
    return d

@pytest.fixture(params=[
    ("rupalirupali1@gmail.com" , "123456" , "Pass"),
    ("rup1alirupali1@gmail.com" , "123456", "Fail"),
    ("rupalirupali1@gmail.com" , "123156" , "Fail"),
    ("rupalir1upali1@gmail.com" , "1234156" , "Fail"),
])

def readLoginData(request):
    return request.param