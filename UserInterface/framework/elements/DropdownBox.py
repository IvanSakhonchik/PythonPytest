from selenium.webdriver.common.by import By

from framework.elements.BaseElement import BaseElement
from selenium.webdriver.support.ui import Select

from framework.utilities.browser.DriverUtils import DriverUtils


class DropdownBox(BaseElement):
    def __init__(self, locator, name):
        super().__init__(locator, name)

    def select_option(self, name):
        self.click()
        dropdown_item = DriverUtils.get_webdriver().find_element(By.XPATH, f"//div[@class='dropdown__list-item' and text()='{name}']")
        dropdown_item.click()
