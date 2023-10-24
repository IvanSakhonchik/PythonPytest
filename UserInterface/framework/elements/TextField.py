from framework.elements.BaseElement import BaseElement
from framework.utilities.logging_config import *


class TextField(BaseElement):
    def __init__(self, locator, name):
        super().__init__(locator, name)

    def send_keys(self, text):
        logging.info(f"Send keys to {self.name}")
        element = self.get_web_element()
        element.clear()
        element.send_keys(text)
