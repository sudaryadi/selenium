from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path='../guru99bank/browser/chromedriver')
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path='../guru99bank/browser/geckodriver')
    else:
        driver = webdriver.Chrome(executable_path='../guru99bank/browser/chromedriver')
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


######### Pytest HTML Report ###########

# It is hook for adding environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Guru99 Bank Apps'
    config._metadata['Module Name'] = 'Test as Manager'
    config._metadata['Tester'] = 'Sbastian Sudaryadi'
    config._metadata['Build'] = '0.0.1'

# It is hook for delete/modify environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA.HOME", None)
    metadata.pop("Plugins", None)
