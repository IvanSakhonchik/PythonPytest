from selenium.webdriver.common.by import By

from framework.elements.Button import Button
from tests.forms.BaseForm import BaseForm


class MainPage(BaseForm):
    __alerts_frame_windows_button = Button((By.XPATH, "//*[contains(text(),'Alerts')]"), "Alerts, Frame & Windows")
    __elements_button = Button((By.XPATH, "//*[text()='Elements']"), "Elements")

    def __init__(self):
        super().__init__((By.XPATH, "//img[@alt='Selenium Online Training']"), "Main page title")

    def click_alerts_frame_windows(self):
        self.__alerts_frame_windows_button.click()

    def click_elements(self):
        self.__elements_button.click()
