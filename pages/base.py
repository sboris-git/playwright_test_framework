from playwright.sync_api import Page
from stage_config import BASE_URL


class Base(object):
    def __init__(self, page: Page):
        self.page = page
        self.base_url = BASE_URL

    def navigate(self) -> None:
        """Navigate to the login page."""
        self.page.goto(f"{self.base_url}")

    def login_button(self):
        return self.page.get_by_role("button", name="Log In")

