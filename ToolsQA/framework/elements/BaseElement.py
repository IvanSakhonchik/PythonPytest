from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from framework.utilities.browser.DriverUtils import DriverUtils
from framework.utilities.config_manager import config_data

from framework.utilities.logging_config import *


class BaseElement:
    def __init__(self, locator, name):
        self.locator = locator
        self.name = name

    def is_visible(self):
        logging.info(f"Chect that {self.name} is visible")
        return len(self.get_web_elements()) != 0

    def wait_until_visible(self):
        logging.info(f"Wait until {self.name} should be visible")
        driver = DriverUtils.get_webdriver()
        wait = WebDriverWait(driver, config_data["wait_element_time"])
        try:
            wait.until(EC.visibility_of_element_located(self.locator))
            return True
        except TimeoutException:
            return False

    def click(self):
        logging.info(f"Click to {self.name}")
        self.get_web_element().click()

    def get_attribute(self, name):
        logging.info(f"Get attribute from {self.name}")
        return self.get_web_element().get_attribute(name)

    def send_keys(self, text):
        logging.info(f"Send keys to {self.name}")
        self.get_web_element().send_keys(text)

    def get_text(self):
        logging.info(f"Get text from {self.name}")
        return self.get_web_element().text

    def get_web_element(self):
        return DriverUtils.get_webdriver().find_element(*self.locator)

    def get_web_elements(self):
        return DriverUtils.get_webdriver().find_elements(*self.locator)
