from framework.utilities.AlertUtils import AlertUtils
from framework.utilities.RandomStringUtils import RandomStringUtils
from framework.utilities.config_manager import test_data
from tests.forms.AlertsForm import AlertsForm
from tests.forms.AlertsFrameWindowsForm import AlertsFrameWindowsForm
from tests.forms.MainPage import MainPage


class TestAlert:
    main_page = MainPage()
    alerts_frame_windows_form = AlertsFrameWindowsForm()
    alerts_form = AlertsForm()

    def test_alerts(self, browser):
        assert self.main_page.is_page_opened(), "The main page is not opened"
        self.main_page.click_alerts_frame_windows()
        self.alerts_frame_windows_form.click_alerts()
        self.alerts_form.click_alert()
        alert_text = AlertUtils.get_text_from_alert()
        assert alert_text == test_data["alert_text"], "The alert text is incorrect"
        AlertUtils.accept_alert()
        assert AlertUtils.is_alert_closed(), "The alert is not closed"

        self.alerts_form.click_confirm()
        confirm_alert_text = AlertUtils.get_text_from_alert()
        assert confirm_alert_text == test_data["confirm_alert_text"], "The confirm alert text is incorrect"
        AlertUtils.accept_alert()
        assert AlertUtils.is_alert_closed(), "The alert is not closed"
        confirm_result_text = self.alerts_form.get_confirm_result()
        assert confirm_result_text == test_data["result_confirm_text"], "The confirm result text is incorrect"

        self.alerts_form.click_prompt()
        prompt_alert_text = AlertUtils.get_text_from_alert()
        assert prompt_alert_text == test_data["prompt_alert_text"], "The prompt alert text is incorrect"
        random_text = RandomStringUtils.generate_random_string()
        AlertUtils.send_keys_to_alert(random_text)
        AlertUtils.accept_alert()
        assert AlertUtils.is_alert_closed(), "The alert is not closed"
        prompt_result_text = self.alerts_form.get_prompt_result()
        expected_prompt_result_text = test_data["prompt_result_text"] + random_text
        assert prompt_result_text == expected_prompt_result_text, "The prompt result text is incorrect"
