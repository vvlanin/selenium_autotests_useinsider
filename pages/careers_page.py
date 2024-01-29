from helpers.locators import CareersPageLocators, CareersQAPageLocators, CareersOpenPosLocators
from pages.base_page import BasePage
from test_data.test_data import Locations, Departments, Urls


class CareersPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def check_teams_blocks(self):
        self.move_to_element_js(*CareersPageLocators.TEAMS)
        assert self.wait_for_element_availability(*CareersPageLocators.TEAMS).is_displayed()

    def check_locations_blocks(self):
        self.move_to_element_js(*CareersPageLocators.LOCATION)
        assert self.wait_for_element_availability(*CareersPageLocators.LOCATION).is_displayed()

    def check_life_at_insider_blocks(self):
        self.move_to_element_js(*CareersPageLocators.LIFE_AT_INSIDER)
        self.wait_for_element_availability(*CareersPageLocators.LIFE_AT_INSIDER).is_displayed()


class CareersQAPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def click_all_qa_jobs_btn(self):
        self.wait_for_element_availability(*CareersQAPageLocators.BTN_SEE_ALL_JOBS).click()


class CareersOpenedPositionsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def select_location(self):
        self.wait_for_element_availability(*CareersOpenPosLocators.DROPDOWN_LOCATION)
        self.select_option_by_text_dropdown(Locations.ISTANBUL, *CareersOpenPosLocators.DROPDOWN_LOCATION)

    def select_department(self):
        self.wait_for_element_availability(*CareersOpenPosLocators.DROPDOWN_DEPARTMENT)
        self.select_option_by_text_dropdown(Departments.QA, *CareersOpenPosLocators.DROPDOWN_DEPARTMENT)

    def check_job_list_presence(self):
        self.move_to_element_js(*CareersOpenPosLocators.JOBS_LIST)
        self.wait_for_element_availability(*CareersOpenPosLocators.JOBS_LIST)

    def check_job_position_elements_text(self):
        # test fails here. To make it passed use 'Software' instead of Departments.QA
        self.check_text_for_similar_elements(CareersOpenPosLocators.POS_TITLE, Departments.QA)

    def check_job_department_elements_text(self):
        self.check_text_for_similar_elements(CareersOpenPosLocators.POS_DEPARTMENT, Departments.QA)

    def check_job_location_elements_text(self):
        self.check_text_for_similar_elements(CareersOpenPosLocators.POS_LOCATION, Locations.ISTANBUL)

    def click_view_role_btn(self):
        self.move_to_element_js(*CareersOpenPosLocators.BTN_VIEW_ROLE)
        self.click_element_js(*CareersOpenPosLocators.BTN_VIEW_ROLE)

    def check_redirect(self):
        self.wait_for_open_new_windows(2)
        self.switch_to_window(1)
        assert Urls.OUTER_PAGE_URL in self.browser.current_url
