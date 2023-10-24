from selenium.webdriver.common.by import By

from framework.elements.Button import Button
from framework.elements.CheckBox import CheckBox
from framework.elements.DropdownBox import DropdownBox
from framework.elements.TextField import TextField
from tests.forms.BaseForm import BaseForm


class FirstCardForm(BaseForm):
    __input_password_text_field = TextField((By.CSS_SELECTOR, "input[placeholder='Choose Password']"),"Password Field")
    __input_email_text_field = TextField((By.CSS_SELECTOR, "input[placeholder='Your email']"), "Email Field")
    __input_domain_text_field = TextField((By.CSS_SELECTOR, "input[placeholder='Domain']"), "Domain Field")
    __domain_name_dropdown_box = DropdownBox((By.CSS_SELECTOR, ".dropdown__field"), "Domain Name")
    __terms_and_conditions_check_box = CheckBox((By.CSS_SELECTOR, ".checkbox__box"), "Terms & Conditions")
    __next_button = Button((By.XPATH, "//a[@class='button--secondary']"), "Next")

    def __init__(self):
        super().__init__((By.XPATH, "//div[@class='page-indicator' and text()='1 / 4']"), "First card title")

    def click_next(self):
        self.__next_button.click()

    def set_password(self, password):
        self.__input_password_text_field.send_keys(password)

    def set_email(self, email):
        self.__input_email_text_field.send_keys(email)

    def set_domain(self, domain):
        self.__input_domain_text_field.send_keys(domain)

    def accept_terms_and_conditions(self):
        self.__terms_and_conditions_check_box.click()

    def select_domain_name(self, domain_name):
        self.__domain_name_dropdown_box.select_option(domain_name)

