from selenium.webdriver.common.by import By

from framework.elements.Button import Button
from framework.elements.Label import Label
from tests.forms.BaseForm import BaseForm


class WelcomePage(BaseForm):
    __hide_button = Button((By.CSS_SELECTOR, ".highlight"), "Hide")
    __accept_cookies_button = Button((By.XPATH, "//*[text()='Not really, no']"), "Not really, no")
    __timer_label = Label((By.CSS_SELECTOR, ".timer"), "Timer")

    def __init__(self):
        super().__init__((By.CSS_SELECTOR, ".logo__icon"), "Welcome page title")

    def hide_help_form(self):
        self.__hide_button.click()

    def is_help_form_hidden(self):
        return not(self.__hide_button.wait_until_not_visible())

    def accept_cookies(self):
        self.__accept_cookies_button.wait_until_visible()
        self.__accept_cookies_button.click()

    def is_cookies_form_closed(self):
        return not(self.__accept_cookies_button.wait_until_not_visible())

    def get_timer_value(self):
        return self.__timer_label.get_text()
