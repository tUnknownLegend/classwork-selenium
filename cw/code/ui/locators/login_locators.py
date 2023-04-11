from selenium.webdriver.common.by import By
from ui.locators.base_locators import BaseLocators


class LoginPageLocators(BaseLocators):
    OPEN_BUTTON_LOGIN_PAGE = (By.XPATH,
                              '/html/body/div[1]/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[1]')

    EMAIL_INPUT_LOGIN_PAGE = (By.NAME, 'email')

    PASSWORD_INPUT_LOGIN_PAGE = (By.NAME, 'password')

    SIGN_IN_BUTTON_LOGIN_PAGE = (By.XPATH,
                                 '/html/body/div[2]/div/div[2]/div/div[4]/div[1]')

    HEADER_EMAIL_LOGIN_PAGE = (By.CLASS_NAME,
                               'right-module-userNameWrap-3Odw2D')
