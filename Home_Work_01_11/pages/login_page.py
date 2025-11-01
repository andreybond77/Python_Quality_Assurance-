# pages.login_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import log_calls # Импортируем декоратор

class LoginPage(BasePage):
    """Страница логина"""

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    @log_calls # Добавляем логирование
    def open_login_page(self):
        self.open("https://www.saucedemo.com")

    @log_calls # Добавляем логирование
    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    @log_calls # Добавляем логирование
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)