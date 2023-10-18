from framework.utilities.browser.DriverUtils import DriverUtils
from tests.forms.AlertsFrameWindowsForm import AlertsFrameWindowsForm
from tests.forms.BrowserWindowsForm import BrowserWindowsForm
from tests.forms.ElementsForm import ElementsForm
from tests.forms.LinksForm import LinksForm
from tests.forms.MainPage import MainPage
from tests.forms.SamplePage import SamplePage


class TestHandles:
    main_page = MainPage()
    alerts_frame_windows_form = AlertsFrameWindowsForm()
    browser_windows_form = BrowserWindowsForm()
    sample_page = SamplePage()
    elements_form = ElementsForm()
    links_form = LinksForm()

    def test_handles_windows(self, browser):
        assert self.main_page.is_page_opened(), "The main page is not opened"
        self.main_page.click_alerts_frame_windows()
        self.alerts_frame_windows_form.click_browser_windows()
        assert self.browser_windows_form.is_page_opened(), "The browser windows page is not opened"
        self.browser_windows_form.click_new_tab()
        DriverUtils.switch_to_next_window()
        assert self.sample_page.is_page_opened(), "The sample page is not opened"
        DriverUtils.close_window()
        DriverUtils.switch_to_main_window()
        assert self.browser_windows_form.is_page_opened(), "The browser windows page is not opened"
        DriverUtils.go_to_address()
        self.main_page.click_elements()
        self.elements_form.click_links()
        assert self.links_form.is_page_opened(), "The links page is not opened"
        self.links_form.click_home()
        DriverUtils.switch_to_next_window()
        assert self.main_page.is_page_opened(), "The main page is not opened"
        DriverUtils.switch_to_main_window()
        assert self.links_form.is_page_opened(), "The links page is not opened"

