import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):

    def is_opened(self, url, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == url:
                return True

        raise PageNotOpenedExeption(
            f'{url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver = driver

    def render(self, url):
        self.driver.get(url)

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=15):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))
