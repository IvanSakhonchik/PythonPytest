from selenium.webdriver.common.by import By

from framework.elements.Button import Button
from tests.forms.BaseForm import BaseForm


class ElementsForm(BaseForm):
    __web_tables_button = Button((By.XPATH, "//*[contains(text(),'Web Tables')]//ancestor::li[@id='item-3']"), "Web Tables")
    __links_button = Button((By.XPATH, "//*[contains(text(),'Links')]//ancestor::li[@id='item-5']"), "Links")

    def __init__(self):
        super().__init__((By.XPATH, "//div[@class='element-list collapse show']"), "Elements list")

    def click_web_tables(self):
        self.__web_tables_button.click()

    def click_links(self):
        self.__links_button.click()
