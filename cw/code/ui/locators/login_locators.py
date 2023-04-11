from selenium.webdriver.common.by import By
from ui.locators.base_locators import BaseLocators


class LoginPageLocators(BaseLocators):
    OPEN_BUTTON_LOGIN_PAGE = (By.XPATH,
                              '//div[(text()="Log in" or text()="Войти") and ' +
                              'contains(@class, "responseHead-module-button")]')

    EMAIL_INPUT_LOGIN_PAGE = (By.NAME, 'email')

    PASSWORD_INPUT_LOGIN_PAGE = (By.NAME, 'password')

    SIGN_IN_BUTTON_LOGIN_PAGE = (By.XPATH,
                                 '//div[(text()="Log in" or text()="Войти") and ' +
                                 'contains(@class, "authForm-module-button")]')
