from playwright.sync_api import Locator
from playwright.sync_api._generated import ElementHandle

from pages.base import Base


class SignUp(Base):

    @property
    def submit_button(self) -> ElementHandle:
        return self.auth_form.wait_for_selector("#login")

    @property
    def auth_form(self) -> ElementHandle:
        return self.page.wait_for_selector("emailAuth")

    def fill_form(self, user: dict) -> None:
        """Fill out the login form.
        :param user: A user intended for login.
        """
        self.page.get_by_test_id("emailAuth").get_by_label("Email").fill(user["email"])
        self.page.get_by_label("Password").fill(user["password"])

    def navigate_to_sign_up(self) -> Locator:
        return self.page.get_by_test_id("siteMembersDialogLayout").get_by_test_id("buttonElement")
