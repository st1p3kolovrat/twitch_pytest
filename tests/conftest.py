import pytest
from utilities.driver_factory import get_driver
from pages.home_page_steps import HomePage
from pages.common_steps import CommonSteps
from pages.search_result_page_steps import SearchResultPage


@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    driver.get("https://m.twitch.tv/")
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def home_page(driver):
    return HomePage(driver)


@pytest.fixture(scope="function")
def common_steps(driver):
    return CommonSteps(driver)


@pytest.fixture(scope="function")
def search_result_page(driver):
    return SearchResultPage(driver)
