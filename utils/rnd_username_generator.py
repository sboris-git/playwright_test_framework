import logging as logger
import random
import string
import time


def generate_random_email_and_password(domain=None, email_prefix=None):

    domain, email_prefix = set_default(domain, email_prefix)

    email = generate_unique_email(domain, email_prefix)
    password = generate_unique_password()

    creds = {'email': email, 'password': password}
    logger.debug(f"Unique email and password: {creds}")

    return creds


def generate_unique_password():
    password_length = 20
    password = ''.join(random.choices(string.ascii_letters, k=password_length))
    return password


def generate_unique_email(domain, email_prefix):
    epoch_time = int(time.time())
    email = email_prefix + str(epoch_time) + '@' + domain
    return email


def set_default(domain, email_prefix):
    if not domain:
        domain = 'gmail.com'
    if not email_prefix:
        email_prefix = 'testuser'
    return domain, email_prefix
