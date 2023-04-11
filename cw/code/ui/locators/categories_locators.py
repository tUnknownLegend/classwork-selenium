from selenium.webdriver.common.by import By
from ui.locators.base_locators import BaseLocators


class CategoriesPageLocators(BaseLocators):
    BALANCE_CATEGORIES_PAGE = (
        By.CLASS_NAME, 'deposit__payment-form__container')

    STATS_CATEGORIES_PAGE = (
        By.CLASS_NAME, 'statistic-page-nt__no-active-campaigns-text')

    PROFILE_CATEGORIES_PAGE = (
        By.CLASS_NAME, 'profile__list')

    # FEED_CATEGORIES_PAGE = (
    #     By.CLASS_NAME, 'feeds-module-controls-cKRaP3')

    UL_ELEMENT_CATEGORIES_PAGE = (By.XPATH,
                                  '/html/body/div[1]/div[1]/div/div/div/div[2]/ul')
