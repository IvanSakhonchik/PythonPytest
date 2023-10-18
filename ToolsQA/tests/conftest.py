import pytest

from framework.utilities.browser.DriverUtils import DriverUtils


@pytest.fixture
def browser():
    DriverUtils.get_webdriver()
    DriverUtils.maximize()
    DriverUtils.go_to_address()
    yield
    DriverUtils.quit_webdriver()