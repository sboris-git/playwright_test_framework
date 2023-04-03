from config import Config

config = Config()


class User:
    def __init__(self):
        self.email = config.email
        self.password = config.password
