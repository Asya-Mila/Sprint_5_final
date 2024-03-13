from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from conftest import driver


class TestConstructor:
    # переход к разделу «Булки»
    def test_constructor_buns(self, driver):
        driver.find_element(*Locators.SAUCES).click()
        driver.find_element(*Locators.BUNS).click()
        driver.find_element(*Locators.FILLINGS).click()
        driver.find_element(*Locators.BUNS).click()
        assert WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.BUNS_PAGE_NAME))

    # переход к разделу «Соусы»
    def test_constructor_sauces(self, driver):
        driver.find_element(*Locators.SAUCES).click()
        assert WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.SAUCES_PAGE_NAME))

    # переход к разделу «Начинки»
    def test_constructor_fillings(self, driver):
        driver.find_element(*Locators.FILLINGS).click()
        assert WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(Locators.FILLINGS_PAGE_NAME))
