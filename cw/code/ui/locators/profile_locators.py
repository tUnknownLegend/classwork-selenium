from selenium.webdriver.common.by import By
from ui.locators.base_locators import BaseLocators


class ProfilePageLocators(BaseLocators):
    PHONE_INPUT_PROFILE_PAGE = (
        By.XPATH, '//div[@class="js-contacts-field-phone profile__list__row__input"]/div/div/input')

    NAME_INPUT_PROFILE_PAGE = (
        By.XPATH, '//div[@class="input" and @data-name = "fio"]/div/input')

    SUBMIT_UPDATE_PROFILE_PAGE = (
        By.XPATH, '//button[@class="button button_submit" and @data-class-name="Submit"]')

    # PHONE_INPUT_PROFILE_PAGE = (By.XPATH,
    #                             '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/ul/li[4]/div[1]/div/div/input')

    # NAME_INPUT_PROFILE_PAGE = (By.XPATH,
    #                            '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/ul/li[2]/div[1]/div/div/input')

    # SUBMIT_UPDATE_PROFILE_PAGE = (By.XPATH,
    #                               '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/button')
