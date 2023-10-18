from selenium.webdriver.common.by import By

from framework.elements.Button import Button
from framework.elements.Label import Label
from tests.forms.BaseForm import BaseForm


class AlertsForm(BaseForm):
    __alert_button = Button((By.CSS_SELECTOR, "#alertButton"), "Alert")
    __confirm_button = Button((By.CSS_SELECTOR, "#confirmButton"), "Confirm alert")
    __confirm_result_label = Label((By.CSS_SELECTOR, "#confirmResult"), "Confirm result")
    __prompt_button = Button((By.CSS_SELECTOR, "#promtButton"), "Prompt")
    __prompt_result_label = Label((By.CSS_SELECTOR, "#promptResult"), "Prompt result")

    def __init__(self):
        super().__init__((By.XPATH, "//div[@class='main-header' and text()='Alerts']"), "Alerts title")

    def click_alert(self):
        self.__alert_button.click()

    def click_confirm(self):
        self.__confirm_button.click()

    def click_prompt(self):
        self.__prompt_button.click()

    def get_confirm_result(self):
        return self.__confirm_result_label.get_text()

    def get_prompt_result(self):
        return self.__prompt_result_label.get_text()
