from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from conftest import driver

accaunt_email = 'Malgina_6@gmail.com'
accaunt_password = '1q2w2q1w'


class TestLogin:
    # вход по кнопке «Войти в аккаунт» на главной
    def test_login_button_main_page(self, driver):
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.REGISTRATION_URL))
        driver.find_element(*Locators.EMAIL_2).send_keys(accaunt_email)
        driver.find_element(*Locators.PASSWORD_2).send_keys(accaunt_password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        assert WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))

    # вход через кнопку «Личный кабинет»
    def test_login_button_personal_acсaunt(self, driver):
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.REGISTRATION_URL))
        driver.find_element(*Locators.EMAIL_2).send_keys(accaunt_email)
        driver.find_element(*Locators.PASSWORD_2).send_keys(accaunt_password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        assert WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))

    # вход через кнопку в форме регистрации
    def test_login_registration_form(self, driver):
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        driver.find_element(*Locators.REGISTRATION_LINK).click()
        driver.find_element(*Locators.LOGIN_LINK).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.REGISTRATION_URL))
        driver.find_element(*Locators.EMAIL_2).send_keys(accaunt_email)
        driver.find_element(*Locators.PASSWORD_2).send_keys(accaunt_password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        assert WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))

    # вход через кнопку в форме восстановления пароля
    def test_login_password_form_recovery(self, driver):
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.PASSWORD_LINK).click()
        driver.find_element(*Locators.LOGIN_LINK).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.REGISTRATION_URL))
        driver.find_element(*Locators.EMAIL_2).send_keys(accaunt_email)
        driver.find_element(*Locators.PASSWORD_2).send_keys(accaunt_password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        assert WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
