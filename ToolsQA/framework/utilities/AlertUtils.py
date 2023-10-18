from selenium.common import NoAlertPresentException
from selenium.webdriver.common.alert import Alert

from framework.utilities.browser.DriverUtils import DriverUtils
from framework.utilities.logging_config import *


class AlertUtils:
    @staticmethod
    def get_alert():
        driver = DriverUtils.get_webdriver()
        return Alert(driver)

    @staticmethod
    def accept_alert():
        logging.info("Accept to alert")
        alert = AlertUtils.get_alert()
        alert.accept()

    @staticmethod
    def dismiss_alert():
        logging.info("Dismiss to alert")
        alert = AlertUtils.get_alert()
        alert.dismiss()

    @staticmethod
    def get_text_from_alert():
        logging.info("Get text from alert")
        alert = AlertUtils.get_alert()
        return alert.text

    @staticmethod
    def send_keys_to_alert(text):
        logging.info("Send keys to alert")
        alert = AlertUtils.get_alert()
        alert.send_keys(text)

    @staticmethod
    def is_alert_closed():
        logging.info("Check that alert is closed")
        try:
            driver = DriverUtils.get_webdriver()
            alert = driver.switch_to.alert
            return False
        except NoAlertPresentException:
            return True
