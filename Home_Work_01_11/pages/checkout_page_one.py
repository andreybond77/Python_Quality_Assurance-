# pages.checkout_page_one.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.logger import log_calls # Импортируем декоратор

class CheckoutPageOne(BasePage):
    """Page Object Model для страницы оформления заказа - Шаг 1 (Информация о покупателе)."""

    TITLE_LOCATOR = (By.CLASS_NAME, "title")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.CLASS_NAME, "cart_cancel_link")

    @log_calls # Добавляем логирование
    def is_loaded(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.TITLE_LOCATOR))
            title_text = self.get_text(self.TITLE_LOCATOR)
            return title_text == "Checkout: Your Information"
        except:
            return False

    @log_calls # Добавляем логирование
    def get_page_title_text(self):
        return self.get_text(self.TITLE_LOCATOR)

    @log_calls # Добавляем логирование
    def fill_customer_info(self, first_name, last_name, postal_code):
        self.type(self.FIRST_NAME_INPUT, first_name)
        self.type(self.LAST_NAME_INPUT, last_name)
        self.type(self.POSTAL_CODE_INPUT, postal_code)

    @log_calls # Добавляем логирование
    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    @log_calls # Добавляем логирование
    def click_cancel(self):
        self.click(self.CANCEL_BUTTON)
