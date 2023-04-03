import os


class Config:

    def __init__(self):
        env = os.environ.get("ENV", "production")
        self.email = os.environ.get("EMAIL", "edu.test.profile@gmail.com")
        self.password = os.environ.get("PASSWORD", "")

        if env == "production":
            self.url = "https://accounts.google.com/"
        elif env == "staging":
            self.url = "https://staging-accounts.google.com/"
        else:
            self.url = "https://localhost:8000/"

    def set_env(self, env):
        if env == "production":
            self.url = "https://accounts.google.com/"
        elif env == "staging":
            self.url = "https://staging-accounts.google.com/"
        else:
            self.url = "https://localhost:8000/"

    @property
    def get_email(self):
        return self.email

    @property
    def get_password(self):
        return self.password
