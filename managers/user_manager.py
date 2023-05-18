from utils.rnd_username_generator import generate_random_email_and_password as unique_user


class User:
    def __init__(self, email=None, password=None):
        self.email = email
        self.password = password

    def create_new_user(self):
        return unique_user(self.email)
