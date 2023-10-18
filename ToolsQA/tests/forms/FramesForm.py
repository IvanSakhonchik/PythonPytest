from selenium.webdriver.common.by import By

from framework.elements.Label import Label
from framework.utilities.FrameUtils import FrameUtils
from tests.forms.BaseForm import BaseForm


class FramesForm(BaseForm):
    __upper_frame_locator = (By.XPATH, '//iframe[@id="frame1"]')
    __lower_frame_locator = (By.XPATH, '//iframe[@id="frame2"]')
    __frame_head_label = Label((By.CSS_SELECTOR, "#sampleHeading"), "Sample Heading")

    def __init__(self):
        super().__init__((By.XPATH, "//div[@class='main-header' and text()='Frames']"), "Frames form title")

    def get_text_from_upper_frame(self):
        return self.get_text_from_frame(self.__upper_frame_locator)

    def get_text_from_lower_frame(self):
        return self.get_text_from_frame(self.__lower_frame_locator)

    def get_text_from_frame(self, locator):
        FrameUtils.switch_to_frame(locator)
        frame_text = self.__frame_head_label.get_text()
        FrameUtils.go_out_frame()
        return frame_text
