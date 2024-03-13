from selenium.webdriver.common.by import By


class Locators:
    # Для тестов регистрации
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, ".//a[@href='/account']")  # кнопка "Личный кабинет"
    LINK_TO_FORM_REGISTRATION = (By.XPATH, ".//a[@href='/register']")  # ссылка на форму регистрации
    NAME = (By.XPATH, ".//h2[text()='Регистрация']/..//label[text() = 'Имя']/../input")  # Поле name
    EMAIL = (By.XPATH, ".//h2[text()='Регистрация']/..//label[text() = 'Email']/../input")  # Поле email
    PASSWORD = (By.XPATH, ".//h2[text()='Регистрация']/..//label[text() = 'Пароль']/../input")  # Поле password
    BUTTON_REGISTRATION = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # кнопка "Зарегистрироваться"
    ERROR_INCORRECT_PASSWORD = (
        By.XPATH, ".//p[text()='Некорректный пароль']")  # Cообщение об ошибке 'Некорреткный пароль'

    # Для тестов входа на страницу
    BUTTON_LOGIN = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # кнопка "Войти в аккаунт"
    REGISTRATION_URL = (By.XPATH, ".//a[@href='/register']")  # ссылка в "Зарегистрироваться"
    EMAIL_2 = (By.XPATH, ".//h2[text()='Вход']/..//label[text() = 'Email']/../input")  # Поле email
    PASSWORD_2 = (By.XPATH, ".//h2[text()='Вход']/..//label[text() = 'Пароль']/../input")  # Поле password
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")  # кнопка "Войти"
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")  # кнопка "Оформить заказ" на главной странице
    REGISTRATION_LINK = By.LINK_TEXT, "Зарегистрироваться"  # По ссылке "Зарегистрироваться"
    LOGIN_LINK = By.LINK_TEXT, "Войти"  # По ссылке "Войти"
    PASSWORD_LINK = By.LINK_TEXT, "Восстановить пароль"  # По ссылке "Восстановить пароль"

    # Для тестирования переходов по станице
    ACCAUNT_BUTTON = By.LINK_TEXT, "Личный Кабинет"
    CONSTRUCTOR = By.LINK_TEXT, "Конструктор"
    LOGO = By.XPATH, '//*[@id="root"]//div[@class="AppHeader_header__logo__2D0X2"]/a[@href="/"]'
    BUTTON_EXIT = (By.XPATH, ".//button[text()='Выход']")

    # Для тестирования конструктора
    BUNS = By.XPATH, ".//span[text()='Булки']"
    BUNS_PAGE_NAME = By.XPATH, ".//h2[text()='Булки']"
    SAUCES = By.XPATH, ".//span[text()='Соусы']"
    SAUCES_PAGE_NAME = By.XPATH, ".//h2[text()='Соусы']"
    FILLINGS = By.XPATH, ".//span[text()='Начинки']"
    FILLINGS_PAGE_NAME = By.XPATH, ".//h2[text()='Начинки']"