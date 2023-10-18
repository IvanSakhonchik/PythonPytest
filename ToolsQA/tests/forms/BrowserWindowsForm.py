from selenium.webdriver.common.by import By

from framework.elements.Button import Button
from tests.forms.BaseForm import BaseForm


class BrowserWindowsForm(BaseForm):
    __new_tab_button = Button((By.CSS_SELECTOR, "#tabButton"), "New tab")

    def __init__(self):
        super().__init__((By.XPATH, "//div[@class='main-header' and text()='Browser Windows']"), "Browser Windows title")

    def click_new_tab(self):
        self.__new_tab_button.click()
