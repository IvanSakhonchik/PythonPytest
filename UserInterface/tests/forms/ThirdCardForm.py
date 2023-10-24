from selenium.webdriver.common.by import By

from tests.forms.BaseForm import BaseForm


class ThirdCardForm(BaseForm):
    def __init__(self):
        super().__init__((By.XPATH, "//div[@class='page-indicator' and text()='3 / 4']"), "Third card title")
