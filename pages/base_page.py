from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from helpers.locators import BasePageLocators


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def accept_cookies(self):
        self.browser.find_element(*BasePageLocators.BTN_ACCEPT_COOKIES).click()

    def click_on_company_element(self):
        self.browser.find_element(*BasePageLocators.NAV_BAR_SELECTOR_COMPANY_ITEM).click()

    def select_careers(self):
        self.browser.find_element(*BasePageLocators.CAREERS_MENU_ITEM).click()

    def open(self, url):
        self.browser.get(url)

    def maximize(self):
        self.browser.maximize_window()

    def wait_for_element_availability(self, *locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(lambda x: x.find_element(*locator))

    def wait_for_element_visibility(self, locator, timeout=100):
        return WebDriverWait(self.browser, timeout).until(
            ec.visibility_of_any_elements_located(locator))

    def wait_company_item(self):
        return self.wait_for_element_availability(*BasePageLocators.NAV_BAR_SELECTOR_COMPANY_ITEM)

    def move_to_element_js(self, *locator):
        element = self.browser.find_element(*locator)
        self.browser.execute_script("arguments[0].scrollIntoView();", element)

    def click_element_js(self, *locator):
        element = self.browser.find_element(*locator)
        self.browser.execute_script("arguments[0].click();", element)

    def select_option_by_text_dropdown(self, option_value, *locator):
        element = Select(self.browser.find_element(*locator))
        element.select_by_visible_text(option_value)

    def get_text_from_similar_elements(self, *locator):
        elements = self.browser.find_elements(*locator)
        for el in elements:
            yield el.text

    def check_text_for_similar_elements(self, locator, text_to_check):
        self.move_to_element_js(*locator)
        self.wait_for_element_visibility(locator)
        txt = list(self.get_text_from_similar_elements(*locator))

        assert all(map(lambda x: text_to_check in x, txt))

    def wait_for_open_new_windows(self, number_of_windows, timeout=10):
        WebDriverWait(self.browser, timeout).until(ec.number_of_windows_to_be(number_of_windows))

    def switch_to_window(self, window_handle):
        self.browser.switch_to.window(self.browser.window_handles[window_handle])
