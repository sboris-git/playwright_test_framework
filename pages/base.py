from config import Config


class BasePage:
    def __init__(self, page):
        self.page = page
        self.config = Config()
