import pytest
from playwright.sync_api import Page

from managers.user_manager import User
from pages.start.login.sign_up import SignUp
# from pages.start.profile import Profile
from pages.base import Base


@pytest.mark.authentication
@pytest.mark.bookstore
class TestSignin:
    def test_valid_login(self, page: Page) -> None:
        """Sign in with valid credentials as a new user.
        :param page: A Playwright browser page.
        """
        page.context.clear_cookies()
        start_page = Base(page)
        sign_up_page = SignUp(page)
        # profile_page = Profile(page)

        start_page.navigate()
        start_page.login_button().click()

        sign_up_page.navigate_to_sign_up().click()
        sign_up_page.fill_form(User.create_new_user())
        sign_up_page.submit_button.click()

        # visible: bool = profile_page.username_value_field.is_visible()

        # assert "profile" in page.url and visible