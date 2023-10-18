from selenium.webdriver.common.by import By

from framework.elements.Button import Button
from framework.elements.Label import Label
from tests.forms.BaseForm import BaseForm


class WebTablesForm(BaseForm):
    __add_button = Button((By.CSS_SELECTOR, "#addNewRecordButton"), "Add")

    def __init__(self):
        super().__init__((By.XPATH, "//div[@class='main-header' and text()='Web Tables']"), "Frames form title")

    def click_add(self):
        self.__add_button.click()

    def is_user_presented(self, user):
        return self.get_delete_button(user).is_visible()

    def delete_user(self,user):
        self.get_delete_button(user).click()

    def get_delete_button(self, user):
        xpath_button = (
            f"//*[text()='{user.first_name}']/following-sibling::*"
            f"[text()='{user.second_name}']/following-sibling::*"
            f"[text()='{user.age}']/following-sibling::*"
            f"[text()='{user.email}']/following-sibling::*"
            f"[text()='{user.salary}']/following-sibling::*"
            f"[text()='{user.department}']/following-sibling::"
            f"*/descendant::*[@title='Delete']"
        )
        return Button((By.XPATH, xpath_button), f"User id: {user.user_id}")
