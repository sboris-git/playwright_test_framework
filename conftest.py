import pytest
from playwright.sync_api import Playwright
from config import Config
from managers.browser_factory import BrowserFactory


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="development", help="Environment to run the tests in")


@pytest.fixture(scope="module")
def browser_factory(request, playwright: Playwright) -> Playwright:
    env = request.config.getoption("--env")
    config = Config()
    config.set_env(env)
    factory = BrowserFactory(config)
    browser = factory.launch_browser(playwright)
    yield browser
    factory.close_browser(browser)
