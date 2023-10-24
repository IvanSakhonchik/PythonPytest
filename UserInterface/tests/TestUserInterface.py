from framework.utilities.EmulatorUtils import EmulatorUtils
from framework.utilities.StringUtils import StringUtils
from framework.utilities.config_manager import test_data
from tests.forms.FirstCardForm import FirstCardForm
from tests.forms.MainPage import MainPage
from tests.forms.SecondCardForm import SecondCardForm
from tests.forms.ThirdCardForm import ThirdCardForm
from tests.forms.WelcomePage import WelcomePage
from tests.utilities.GenerateDataUtils import GenerateDataUtils


class TestUserInterface:
    main_page = MainPage()
    first_card_form = FirstCardForm()
    second_card_form = SecondCardForm()
    third_card_form = ThirdCardForm()
    welcome_page = WelcomePage()

    def test_cards(self, browser):
        assert self.main_page.is_page_opened(), "The main page is not opened"
        self.main_page.click_next()
        assert self.first_card_form.is_page_opened(), "The first card is not opened"

        email = StringUtils.generate_random_string()
        password = GenerateDataUtils.generate_password(email)
        domain = StringUtils.generate_random_string()
        domain_name = GenerateDataUtils.generate_dropdown()

        self.first_card_form.set_password(password)
        self.first_card_form.set_email(email)
        self.first_card_form.set_domain(domain)
        self.first_card_form.select_domain_name(domain_name)
        self.first_card_form.accept_terms_and_conditions()
        self.first_card_form.click_next()
        assert self.second_card_form.is_page_opened(), "The second card is not opened"

        self.second_card_form.unselect_all_interest()
        interests = GenerateDataUtils.generate_interests()
        self.second_card_form.select_interests(interests)
        self.second_card_form.click_upload()
        EmulatorUtils.input_image()
        self.second_card_form.click_next()
        assert self.third_card_form.is_page_opened(), "The third card is not opened"

    def test_help_form(self, browser):
        assert self.main_page.is_page_opened(), "The main page is not opened"
        self.main_page.click_next()
        self.welcome_page.is_page_opened(), "Welcome page is not opened"
        self.welcome_page.hide_help_form()
        assert self.welcome_page.is_help_form_hidden(), "Help form is not hidden"

    def test_cookies_form(self, browser):
        assert self.main_page.is_page_opened(), "The main page is not opened"
        self.main_page.click_next()
        self.welcome_page.is_page_opened(), "Welcome page is not opened"
        self.welcome_page.accept_cookies()
        assert self.welcome_page.is_cookies_form_closed(), "Cookies form is not closed"

    def test_timer(self, browser):
        assert self.main_page.is_page_opened(), "The main page is not opened"
        self.main_page.click_next()
        self.welcome_page.is_page_opened(), "Welcome page is not opened"
        actual_timer_value = self.welcome_page.get_timer_value()
        assert actual_timer_value == test_data["timer_value"], "Timer is not correct"
