from selenium.webdriver.common.by import By

from framework.elements.Button import Button
from tests.forms.BaseForm import BaseForm


class AlertsFrameWindowsForm(BaseForm):
    __alerts_button = Button((By.XPATH, "//*[contains(text(),'Alerts')]//ancestor::li[@id='item-1']"), "Alerts")
    __nested_frames_button = Button((By.XPATH, "//*[contains(text(),'Nested Frames')]//ancestor::li[@id='item-3']"), "Nested Frames")
    __frames_button = Button((By.XPATH, "//*[contains(text(),'Frames')]//ancestor::li[@id='item-2']"), "Frames")
    __browser_windows_button = Button((By.XPATH, "//*[contains(text(),'Browser Windows')]//ancestor::li[@id='item-0']"), "BrowserWindows")

    def __init__(self):
        super().__init__((By.XPATH, "//span[text()='Modal Dialogs']"), "Modal Dialogs")

    def click_alerts(self):
        self.__alerts_button.click()

    def click_frames(self):
        self.__frames_button.click()

    def click_nested_frames(self):
        self.__nested_frames_button.click()

    def click_browser_windows(self):
        self.__browser_windows_button.click()
