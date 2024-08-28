import pytest
from utils.browser_manager import BrowserManager


@pytest.fixture(scope="module")
def driver():
    # Instantiate the BrowserManager class
    browser_manager = BrowserManager()

    # Get the WebDriver instance
    driver = browser_manager.get_driver()

    # Yield the WebDriver instance to the tests
    yield driver

    # Quit the driver after the tests have run
    driver.quit()


def test_example(driver):
    driver.get("https://www.hackerrank.com/")
    assert "HackerRank" in driver.title
