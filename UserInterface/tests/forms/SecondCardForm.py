from selenium.webdriver.common.by import By

from framework.elements.Button import Button
from framework.elements.CheckBox import CheckBox
from tests.forms.BaseForm import BaseForm


class SecondCardForm(BaseForm):
    __unselect_all_check_box = CheckBox((By.XPATH, "//*[@for='interest_unselectall']"), "Interest unselect all")
    __upload_button = Button((By.XPATH, "//a[contains(@class,'upload-button')]"), "Upload")
    __next_button = Button((By.XPATH, "//button[text()='Next']"), "Next")

    def __init__(self):
        super().__init__((By.XPATH, "//div[@class='page-indicator' and text()='2 / 4']"), "Second card title")

    def unselect_all_interest(self):
        self.__unselect_all_check_box.click()

    def select_interests(self, interests):
        for interest in interests:
            interest = CheckBox((By.XPATH, f"//span[text()='{interest}']//preceding-sibling::span"), f"{interest}")
            interest.click()

    def click_upload(self):
        self.__upload_button.click()

    def click_next(self):
        self.__next_button.click()
