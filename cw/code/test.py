from selenium.webdriver.common.by import By
import time
import pytest
from ui.fixtures import get_driver
from ui.pages.base_page import BasePage


class LoginPage(BasePage):
    url = 'https://target-sandbox.my.com/'
    email = 'pinvlad00@yandex.com'
    pwd = 'LOL123!'

    def render_page(self):
        self.render(self.url)
        self.is_opened(self.url)

    def login(self):
        self.find(
            (By.XPATH,
             '/html/body/div[1]/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[1]')
        ).click()

        email_field = self.find((By.NAME, 'email'))
        email_field.clear()
        email_field.send_keys(self.email)

        pwd_field = self.find(
            (By.NAME, 'password'))
        pwd_field.clear()
        pwd_field.send_keys(self.pwd)

        self.find(
            (By.XPATH,
             '/html/body/div[2]/div/div[2]/div/div[4]/div[1]')
        ).click()

    def check_header_email(self):
        assert self.find(
            (By.CLASS_NAME,
             'right-module-userNameWrap-3Odw2D'),
            10)


class CategoriesPage(BasePage):
    balance_button = 2
    stats_button = 3
    profile_button = 5
    feed_button = 6
    support_button = 7

    balance_className = 'deposit__payment-form__container'
    stats_className = 'statistic-page-nt__no-active-campaigns-text'
    profile_className = 'profile__list'
    feed_className = 'feeds-module-controls-cKRaP3'

    def get_ul_element(self):
        return self.find(
            (By.XPATH,
             '/html/body/div[1]/div[1]/div/div/div/div[2]/ul'))

    def click_li_element(self, order):
        return self.get_ul_element().find_elements(By.TAG_NAME, 'li')[order].click()

    def checkClassName(self, className):
        assert self.find((By.CLASS_NAME, className), 10)

    def test_header_categories(self, starting_element,
                               starting_element_className,
                               first_destination_element,
                               first_destination_className,
                               second_destination_element,
                               second_destination_className):

        self.click_li_element(starting_element)
        self.checkClassName(starting_element_className)

        self.click_li_element(first_destination_element)
        self.checkClassName(first_destination_className)

        self.click_li_element(starting_element)
        self.checkClassName(starting_element_className)

        self.click_li_element(second_destination_element)
        self.checkClassName(second_destination_className)

    def navigateToProfile(self):
        self.click_li_element(self.profile_button)

    def navigateToFeed(self):
        self.click_li_element(self.feed_button)

    def test_navigation(self):
        self.test_header_categories(self.balance_button,
                                    self.balance_className,
                                    self.stats_button,
                                    self.stats_className,
                                    self.profile_button,
                                    self.profile_className)


class ProfilePage(BasePage):
    phone_number = '+74957256357'
    name = 'ФИО'

    def get_phone_field(self):
        return self.find(
            (By.XPATH,
             '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/ul/li[4]/div[1]/div/div/input'),
            5)

    def get_name_field(self):
        return self.find(
            (By.XPATH,
             '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/ul/li[2]/div[1]/div/div/input'),
            5)

    def change_data(self, phone_number, name):
        phone_field = self.get_phone_field()
        name_field = self.get_name_field()

        phone_field.clear()
        name_field.clear()

        phone_field.send_keys(phone_number)
        name_field.send_keys(name)

        self.find(
            (By.XPATH,
             '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/button')).click()

    def verify_data(self, phone_number, name, doChange):
        if doChange:
            self.change_data(phone_number, name)
        assert phone_number == self.get_phone_field().get_attribute('value')
        assert name == self.get_name_field().get_attribute('value')

    def verify_change_data(self, doChange=True):
        self.verify_data(self.phone_number, self.name, doChange)

    def verify_empty_data(self, doChange=True):
        self.verify_data('', '', doChange)


class TestLogin():
    driver = get_driver('chrome')

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.render_page()
        login_page.login()
        login_page.check_header_email()


class TestCategories():
    driver = get_driver('chrome')

    def test_header_categories(self):
        login_page = LoginPage(self.driver)
        login_page.render_page()
        login_page.login()
        categories_page = CategoriesPage(self.driver)
        categories_page.test_navigation()


class TestChangeProfile():
    driver = get_driver('chrome')

    def reload(self, categories_page):
        categories_page.navigateToFeed()
        categories_page.navigateToProfile()

    def test_change_profile(self):
        login_page = LoginPage(self.driver)
        login_page.render_page()
        login_page.login()
        categories_page = CategoriesPage(self.driver)
        categories_page.navigateToProfile()
        profile_page = ProfilePage(self.driver)
        profile_page.verify_change_data()
        self.reload(categories_page)
        profile_page.verify_change_data(False)
        profile_page.verify_empty_data()
