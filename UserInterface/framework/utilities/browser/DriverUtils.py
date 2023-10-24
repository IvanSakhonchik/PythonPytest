from framework.utilities.browser.BrowserFactory import BrowserFactory
from framework.utilities.config_manager import config_data


class DriverUtils:
    web_driver = None

    @classmethod
    def get_webdriver(cls):
        if cls.web_driver is None:
            cls.web_driver = BrowserFactory.get_browser_webdriver()
        return cls.web_driver

    @classmethod
    def go_to_address(cls, url=config_data["base_url"]):
        cls.web_driver.get(url)

    @classmethod
    def maximize(cls):
        cls.web_driver.maximize_window()

    @classmethod
    def switch_to_next_window(cls):
        window_handles = cls.web_driver.window_handles
        if len(window_handles) > 1:
            cls.web_driver.switch_to.window(window_handles[1])
        else:
            raise Exception("The next window is not exist")

    @classmethod
    def switch_to_main_window(cls):
        window_handles = cls.web_driver.window_handles
        if len(window_handles) > 0:
            cls.web_driver.switch_to.window(window_handles[0])
        else:
            raise Exception("The main window is not exist")

    @classmethod
    def close_window(cls):
        cls.web_driver.close()

    @classmethod
    def get_url(cls):
        return cls.web_driver.current_url

    @classmethod
    def quit_webdriver(cls):
        if cls.web_driver is not None:
            cls.web_driver.quit()
            cls.web_driver = None
