from selenium.webdriver.common.by import By

from framework.elements.Button import Button
from tests.forms.BaseForm import BaseForm


class SamplePage(BaseForm):
    def __init__(self):
        super().__init__((By.CSS_SELECTOR, "#sampleHeading"), "Sample page title")