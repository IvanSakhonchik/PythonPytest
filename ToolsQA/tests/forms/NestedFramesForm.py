from selenium.webdriver.common.by import By

from framework.elements.Label import Label
from framework.utilities.FrameUtils import FrameUtils
from tests.forms.BaseForm import BaseForm


class NestedFramesForm(BaseForm):
    __parent_frame_locator = (By.XPATH, '//iframe[@id="frame1"]')
    __child_frame_locator = (By.XPATH, '//iframe[@srcdoc="<p>Child Iframe</p>"]')
    __frame_body_label = Label((By.TAG_NAME, "body"), "Body")

    def __init__(self):
        super().__init__((By.XPATH, "//div[@class='main-header' and text()='Nested Frames']"), "Frames form title")

    def get_text_from_parent_frame(self):
        return self.get_text_from_frame(self.__parent_frame_locator)

    def get_text_from_child_frame(self):
        return self.get_text_from_frame(self.__child_frame_locator)

    def get_text_from_frame(self, locator):
        FrameUtils.switch_to_frame(locator)
        frame_text = self.__frame_body_label.get_text()
        return frame_text