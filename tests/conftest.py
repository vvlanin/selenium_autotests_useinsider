import pytest
import chromedriver_autoinstaller
from selenium import webdriver


@pytest.fixture()
def browser():
    chromedriver_autoinstaller.install()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-notifications')

    chrome_browser = webdriver.Chrome(options=chrome_options)
    chrome_browser.implicitly_wait(10)
    return chrome_browser

