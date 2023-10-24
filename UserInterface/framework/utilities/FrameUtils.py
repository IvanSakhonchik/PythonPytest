from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from framework.utilities.browser.DriverUtils import DriverUtils
from framework.utilities.config_manager import config_data
from framework.utilities.logging_config import *


class FrameUtils:
    @staticmethod
    def switch_to_frame(locator):
        logging.info(f"Switch to frame by {locator} locator")
        driver = DriverUtils.get_webdriver()
        wait = WebDriverWait(driver, config_data["wait_element_time"])
        frame_element = wait.until(EC.visibility_of_element_located(locator))
        driver.switch_to.frame(frame_element)

    @staticmethod
    def go_out_frame():
        logging.info("Go out frame")
        driver = DriverUtils.get_webdriver()
        driver.switch_to.default_content()
