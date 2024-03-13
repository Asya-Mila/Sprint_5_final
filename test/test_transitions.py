from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from conftest import driver

accaunt_email = 'Malgina_6@gmail.com'
accaunt_password = '1q2w2q1w'


class TestTransitions:
    # переход по клику на «Личный кабинет».
    def test_transitions_personal_accaunt(self, driver):
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.REGISTRATION_URL))
        driver.find_element(*Locators.EMAIL_2).send_keys(accaunt_email)
        driver.find_element(*Locators.PASSWORD_2).send_keys(accaunt_password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.ACCAUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    # Проверь переход по клику на «Конструктор» и на логотип Stellar Burgers.
    def test_transitions_constructor(self, driver):
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.REGISTRATION_URL))
        driver.find_element(*Locators.EMAIL_2).send_keys(accaunt_email)
        driver.find_element(*Locators.PASSWORD_2).send_keys(accaunt_password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.ACCAUNT_BUTTON).click()
        driver.find_element(*Locators.CONSTRUCTOR).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.url_changes('https://stellarburgers.nomoreparties.site/account/profile'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_transitions_logo(self, driver):
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.REGISTRATION_URL))
        driver.find_element(*Locators.EMAIL_2).send_keys(accaunt_email)
        driver.find_element(*Locators.PASSWORD_2).send_keys(accaunt_password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.ACCAUNT_BUTTON).click()
        driver.find_element(*Locators.LOGO).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_changes('https://stellarburgers.nomoreparties.site/account/profile'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    # Проверь выход по кнопке «Выйти» в личном кабинете
    def test_transitions_exit(self, driver):
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.REGISTRATION_URL))
        driver.find_element(*Locators.EMAIL_2).send_keys(accaunt_email)
        driver.find_element(*Locators.PASSWORD_2).send_keys(accaunt_password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.ACCAUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
        driver.find_element(*Locators.BUTTON_EXIT).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.url_changes('https://stellarburgers.nomoreparties.site/account/profile'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
