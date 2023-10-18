from selenium.webdriver.common.by import By

from framework.elements.Button import Button
from framework.elements.TextField import TextField
from tests.forms.BaseForm import BaseForm


class RegistrationForm(BaseForm):
    __first_name_text_field = TextField((By.CSS_SELECTOR, "#firstName"), "First name")
    __second_name_text_field = TextField((By.CSS_SELECTOR, "#lastName"), "Second name")
    __email_text_field = TextField((By.CSS_SELECTOR, "#userEmail"), "Email")
    __age_text_field = TextField((By.CSS_SELECTOR, "#age"), "Age")
    __salary_text_field = TextField((By.CSS_SELECTOR, "#salary"), "Salary")
    __department_text_field = TextField((By.CSS_SELECTOR, "#department"), "Department")
    __submit_button = Button((By.CSS_SELECTOR, "#submit"), "Submit")

    def __init__(self):
        super().__init__((By.CSS_SELECTOR, "#registration-form-modal"), "Registration form modal")

    def fill_form(self, user):
        self.__first_name_text_field.send_keys(user.first_name)
        self.__second_name_text_field.send_keys(user.second_name)
        self.__email_text_field.send_keys(user.email)
        self.__age_text_field.send_keys(user.age)
        self.__salary_text_field.send_keys(user.salary)
        self.__department_text_field.send_keys(user.department)
        self.__submit_button.click()
