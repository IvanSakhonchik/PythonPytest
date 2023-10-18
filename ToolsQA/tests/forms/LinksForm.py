from selenium.webdriver.common.by import By

from framework.elements.Button import Button
from tests.forms.BaseForm import BaseForm


class LinksForm(BaseForm):
    __home_button = Button((By.CSS_SELECTOR, "#simpleLink"), "Home")

    def __init__(self):
        super().__init__((By.XPATH, "//div[@class='main-header' and text()='Links']"), "Alerts title")

    def click_home(self):
        self.__home_button.click()
