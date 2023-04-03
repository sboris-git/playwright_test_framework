from playwright.sync_api import Playwright


class BrowserFactory:
    def __init__(self, browser_name):
        self.browser_name = browser_name

    def launch_browser(self, playwright: Playwright):
        if self.browser_name == 'firefox':
            return playwright.firefox.launch(headless=False)
        elif self.browser_name == 'webkit':
            return playwright.webkit.launch(headless=False)
        else:
            return playwright.chromium.launch(headless=False)

    def close_browser(self, browser):
        browser.close()
