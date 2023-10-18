from framework.utilities.config_manager import test_users
from tests.forms.ElementsForm import ElementsForm
from tests.forms.MainPage import MainPage
from tests.forms.RegistrationForm import RegistrationForm
from tests.forms.WebTablesForm import WebTablesForm


class TestIFrame:
    main_page = MainPage()
    elements_form = ElementsForm()
    web_tables_form = WebTablesForm()
    registration_form = RegistrationForm()

    def test_iframe(self, browser):
        assert self.main_page.is_page_opened(), "The main page is not opened"
        self.main_page.click_elements()
        self.elements_form.click_web_tables()
        assert self.web_tables_form.is_page_opened(), "The web tables page is not opened"
        for user in test_users:
            self.web_tables_form.click_add()
            assert self.registration_form.is_page_opened(), "Registration form is not opened"
            self.registration_form.fill_form(user)
        for user in test_users:
            assert self.web_tables_form.is_user_presented(user), f"The user {user.user_id} is not presented"
        for user in test_users:
            self.web_tables_form.delete_user(user)
            assert not (self.web_tables_form.is_user_presented(user)), f"The user {user.user_id} is not deleted"
