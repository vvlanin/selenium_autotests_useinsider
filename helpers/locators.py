from dataclasses import dataclass


@dataclass(frozen=True)
class BasePageLocators:
    CAREERS_MENU_ITEM = ('xpath', '//a[contains(text(),"Careers")]')
    NAV_BAR_SELECTOR_COMPANY_ITEM = ('xpath', '//a[contains(text(),"Company")]')
    BTN_ACCEPT_COOKIES = ('xpath', '//a[@id="wt-cli-accept-all-btn"]')


@dataclass(frozen=True)
class CareersPageLocators:
    TEAMS = ('id', 'career-find-our-calling')
    LOCATION = ('id', 'career-our-location')
    LIFE_AT_INSIDER = ('xpath', '//div[@class="elementor-swiper"]')


@dataclass(frozen=True)
class CareersQAPageLocators:
    BTN_SEE_ALL_JOBS = ('xpath', '//a[contains(text(),"See all QA jobs")]')


@dataclass(frozen=True)
class CareersOpenPosLocators:
    DROPDOWN_LOCATION = ('name', 'filter-by-location')
    DROPDOWN_DEPARTMENT = ('name', 'filter-by-department')
    JOBS_LIST = ('id', 'jobs-list')
    POS_TITLE = ('xpath', '//p[contains(@class, "position-title")]')
    POS_DEPARTMENT = ('xpath', '//span[contains(@class, "position-department")]')
    POS_LOCATION = ('xpath', '//div[contains(@class, "position-location")]')
    BTN_VIEW_ROLE = ('xpath', '//a[contains(@class, "btn-navy rounded p")]')
    H3 = ('xpath', '//h3[@class="mb-0"]')
