from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from conftest import driver, generate_random_username, generate_random_password, generate_random_email, generate_random_wrong_password


class TestRegistration:
    def test_registration_positive(self, driver, generate_random_username,
                                   generate_random_password, generate_random_email):
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.LINK_TO_FORM_REGISTRATION)).click()
        driver.find_element(*Locators.NAME).send_keys(generate_random_username)
        driver.find_element(*Locators.EMAIL).send_keys(generate_random_email)
        driver.find_element(*Locators.PASSWORD).send_keys(generate_random_password)
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        assert expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON)

    def test_registration_negative(self, driver, generate_random_username,
                                   generate_random_password, generate_random_email, generate_random_wrong_password):
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.LINK_TO_FORM_REGISTRATION)).click()
        driver.find_element(*Locators.NAME).send_keys(generate_random_username)
        driver.find_element(*Locators.EMAIL).send_keys(generate_random_email)
        driver.find_element(*Locators.PASSWORD).send_keys(generate_random_wrong_password)
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        incorrect_password = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.ERROR_INCORRECT_PASSWORD)).text
        assert incorrect_password == 'Некорректный пароль'
