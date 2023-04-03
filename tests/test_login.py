import pytest
from playwright.sync_api import Playwright, Browser
from dto.user import User
from pages.login.login_page import LoginPage


def test_login_negative(browser_factory: Browser, playwright: Playwright):
    user = User()
    login_page = LoginPage(browser_factory.new_page())
    login_page.goto()
    warning_notification = login_page.login_with_not_existing_user(user)

    assert warning_notification is not None


@pytest.mark.skip('There are no valid users yet')
def test_login(browser_factory: Browser, playwright: Playwright):
    user = User()
    login_page = LoginPage(browser_factory.new_page())
    login_page.goto()
    login_page.login(user)

    assert "Inbox" in browser_factory.get_page_title()
