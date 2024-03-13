import random
import string
import pytest
from selenium import webdriver


@pytest.fixture
def generate_random_password(length=6):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_password = ''.join(random.choice(characters) for _ in range(length))
    return random_password


@pytest.fixture
def generate_random_wrong_password(length=5):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_password = ''.join(random.choice(characters) for _ in range(length))
    return random_password


@pytest.fixture
def generate_random_email():
    domains = ['example.com', 'test.com', 'random.com']
    username = ''.join(random.choice(string.ascii_letters) for _ in range(8))
    domain = random.choice(domains)
    random_email = f"{username}@{domain}"
    return random_email


@pytest.fixture
def generate_random_username():
    names = ['Alice', 'Bob', 'Charlie', 'David', 'Emily']
    random_name = random.choice(names)
    return random_name


@pytest.fixture
def driver():
    driver: webdriver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()
