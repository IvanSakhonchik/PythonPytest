from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from framework.utilities.config_manager import config_data


class BrowserFactory:
    @staticmethod
    def get_browser_webdriver():
        name_browser = config_data["browser_type"]
        option_browser = config_data["browser_option"]

        if name_browser.upper() == "CHROME":
            return BrowserFactory.get_chrome_webdriver(option_browser)
        elif name_browser.upper() == "FIREFOX":
            return BrowserFactory.get_firefox_webdriver(option_browser)
        else:
            raise Exception("Incorrect BrowserName")

    @staticmethod
    def get_chrome_webdriver(option_browser):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(option_browser)
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    @staticmethod
    def get_firefox_webdriver(option_browser):
        GeckoDriverManager().install()
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument(option_browser)
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
