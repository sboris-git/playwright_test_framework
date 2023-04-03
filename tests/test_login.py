import pytest
from playwright.sync_api import Playwright, Browser
from dto.user import User
from pages.login.login_page import LoginPage


@pytest.mark.regression
@pytest.mark.negative
def test_login_negative(browser_factory: Browser, playwright: Playwright):
    user = User()
    login_page = LoginPage(browser_factory.new_page())
    login_page.goto()
    resulted_page = login_page.login_with_not_existing_user(user)
    warning_notification_element = resulted_page.get_by_text("Couldn’t find your Google Account")

    assert warning_notification_element is not None, "FAIL: Warning 'Couldn’t find your Google Account'\
     is not on the page"


@pytest.mark.regression
@pytest.mark.smoke
def test_login(browser_factory: Browser, playwright: Playwright):
    user = User()
    login_page = LoginPage(browser_factory.new_page())
    login_page.goto()
    result_page = login_page.login(user)

    assert result_page.title() in 'Sign in - Google Accounts', 'FAIL: log in failed'
