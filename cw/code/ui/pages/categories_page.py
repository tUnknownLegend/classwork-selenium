from ui.pages.base_page import BasePage
from ui.locators.categories_locators import CategoriesPageLocators


class CategoriesPage(BasePage):
    locators = CategoriesPageLocators()

    balance_button = 2
    stats_button = 3
    profile_button = 5
    feed_button = 6
    support_button = 7

    def get_ul_element(self):
        return self.find(
            self.locators.UL_ELEMENT_CATEGORIES_PAGE)

    def click_li_element(self, order):
        return self.get_ul_element().find_elements(
            self.locators.GET_LI_ELEMENT[0],
            self.locators.GET_LI_ELEMENT[1])[order].click()

    def checkClassName(self, classNameSelector):
        assert self.find(classNameSelector, 10)

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
                                    self.locators.BALANCE_CATEGORIES_PAGE,
                                    self.stats_button,
                                    self.locators.STATS_CATEGORIES_PAGE,
                                    self.profile_button,
                                    self.locators.PROFILE_CATEGORIES_PAGE)
