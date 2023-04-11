import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from ui.pages.base_page import BasePage
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


def _options():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--incognito")
    return options


def get_driver(browser_name):
    if browser_name == 'chrome':
        browser = webdriver.Chrome(
            service=ChromeService(
                executable_path=ChromeDriverManager().install()),
            options=_options())
    elif browser_name == 'firefox':
        browser = webdriver.Firefox(
            service=FirefoxService(
                executable_path=GeckoDriverManager().install()))
    else:
        raise RuntimeError(f'Unsupported browser: "{browser_name}"')
    browser.maximize_window()
    return browser


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)
