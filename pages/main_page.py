from pages.base_page import BasePage
from test_data.test_data import Urls, PageTitles


class UserInsiderMainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def check_if_page_opened(self):
        assert self.browser.current_url == Urls.MAIN_PAGE_URL
        assert self.browser.title == PageTitles.MAIN_PAGE_TITLE

