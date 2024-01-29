import pytest

from pages.careers_page import CareersOpenedPositionsPage, CareersQAPage, CareersPage
from pages.main_page import UserInsiderMainPage
from test_data.test_data import Urls


def test_careers_blocks(browser):
    main_page = UserInsiderMainPage(browser)
    main_page.open(Urls.MAIN_PAGE_URL)
    main_page.maximize()
    main_page.check_if_page_opened()

    main_page.accept_cookies()
    main_page.wait_company_item()
    main_page.click_on_company_element()
    main_page.select_careers()

    careers_page = CareersPage(browser)
    careers_page.check_teams_blocks()
    careers_page.check_locations_blocks()
    careers_page.check_life_at_insider_blocks()


@pytest.mark.xfail(reason="not all Positions contain 'Quality Assurance'")
def test_check_job_position(browser):
    careers_qa_page = CareersQAPage(browser)
    careers_qa_page.open(Urls.CAREERS_QA_PAGE_URL)
    careers_qa_page.maximize()

    careers_qa_page.accept_cookies()
    careers_qa_page.click_all_qa_jobs_btn()

    careers_opened_pos_page = CareersOpenedPositionsPage(browser)
    careers_opened_pos_page.select_location()
    careers_opened_pos_page.select_department()
    careers_opened_pos_page.check_job_list_presence()
    careers_opened_pos_page.check_job_position_elements_text()
    careers_opened_pos_page.check_job_department_elements_text()
    careers_opened_pos_page.check_job_location_elements_text()
    careers_opened_pos_page.click_view_role_btn()
    careers_opened_pos_page.check_redirect()

