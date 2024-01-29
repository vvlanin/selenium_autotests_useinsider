from dataclasses import dataclass
from enum import StrEnum


@dataclass(frozen=True)
class Urls:
    MAIN_PAGE_URL = "https://useinsider.com/"
    CAREERS_PAGE_URL = "https://useinsider.com/careers/"
    CAREERS_QA_PAGE_URL = "https://useinsider.com/careers/quality-assurance/"
    OUTER_PAGE_URL = "https://jobs.lever.co/"


@dataclass(frozen=True)
class PageTitles:
    MAIN_PAGE_TITLE = "#1 Leader in Individualized, Cross-Channel CX — Insider"


@dataclass(frozen=True)
class Locations(StrEnum):
    ISTANBUL = 'Istanbul, Turkey'
    KUALA_LUMPUR = 'Kuala Lumpur, Malaysia'
    WARSAW = 'Warsaw, Poland'
    PARIS = 'Paris, France'

    def __str__(self):
        return self.value


@dataclass(frozen=True)
class Departments(StrEnum):
    QA = 'Quality Assurance'
    PM = 'Product Management'
    SALES = 'Sales'

    def __str__(self):
        return self.value
