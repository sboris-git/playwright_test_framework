from pages.base import BasePage
from config import Config


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.email_input = "#identifierId"
        self.password_input = 'input[type="password"]'
        self.next_button = "#identifierNext"
        self.submit_button = '#passwordNext'
        self.config = Config()

    def goto(self):
        self.page.goto(self.config.url)

    def login(self, user=None):
        if user is None:
            email = self.config.email
            password = self.config.password
        else:
            email = user.email
            password = user.password

        self.page.fill(self.email_input, email)
        self.page.click(self.next_button)
        self.page.wait_for_selector(self.password_input)
        self.page.fill(self.password_input, password)
        self.page.click(self.submit_button)

        return self.page

    def login_with_not_existing_user(self, user=None):
        if user is None:
            email = self.config.email
        else:
            email = user.email

        self.page.fill(self.email_input, email)
        self.page.click(self.next_button)

        return self.page
