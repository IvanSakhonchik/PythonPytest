from framework.utilities.FrameUtils import FrameUtils
from framework.utilities.config_manager import test_data
from tests.forms.AlertsFrameWindowsForm import AlertsFrameWindowsForm
from tests.forms.FramesForm import FramesForm
from tests.forms.MainPage import MainPage
from tests.forms.NestedFramesForm import NestedFramesForm


class TestIFrame:
    main_page = MainPage()
    alerts_frame_windows_form = AlertsFrameWindowsForm()
    frames_form = FramesForm()
    nested_frames_form = NestedFramesForm()

    def test_iframe(self, browser):
        assert self.main_page.is_page_opened(), "The main page is not opened"
        self.main_page.click_alerts_frame_windows()

        self.alerts_frame_windows_form.click_frames()
        assert self.frames_form.is_page_opened(), "The frames page is not opened"
        upper_frame_text = self.frames_form.get_text_from_upper_frame()
        lower_frame_text = self.frames_form.get_text_from_lower_frame()
        assert upper_frame_text == lower_frame_text, "The frames text are not match"

        self.alerts_frame_windows_form.click_nested_frames()
        assert self.nested_frames_form.is_page_opened(), "The nested frames page is not opened"
        parent_frame_text = self.nested_frames_form.get_text_from_parent_frame()
        child_frame_text = self.nested_frames_form.get_text_from_child_frame()
        FrameUtils.go_out_frame()
        assert parent_frame_text == test_data["parent_frame_text"], "The parent frame text is not correct"
        assert child_frame_text == test_data["child_frame_text"], "The child frame text is not correct"
