from selenium.webdriver.common.by import By

from framework.elements.Button import Button
from tests.forms.BaseForm import BaseForm


class MainPage(BaseForm):
    __next_button = Button((By.XPATH, "//a[@class='start__link']"), "Next")

    def __init__(self):
        super().__init__((By.CSS_SELECTOR, ".logo__icon"), "Main page title")

    def click_next(self):
        self.__next_button.click()
