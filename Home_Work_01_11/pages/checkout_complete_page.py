# pages.checkout_complete_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.logger import log_calls # Импортируем декоратор

class CheckoutCompletePage(BasePage):
    """Page Object Model для страницы завершения оформления заказа."""

    TITLE_LOCATOR = (By.CLASS_NAME, "title")
    CONFIRMATION_MESSAGE_LOCATOR = (By.CLASS_NAME, "complete-header")
    SUB_MESSAGE_LOCATOR = (By.CLASS_NAME, "complete-text")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")

    @log_calls # Добавляем логирование
    def is_loaded(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.TITLE_LOCATOR))
            title_text = self.get_text(self.TITLE_LOCATOR)
            return title_text == "Checkout: Complete!"
        except:
            return False

    @log_calls # Добавляем логирование
    def get_page_title_text(self):
        return self.get_text(self.TITLE_LOCATOR)

    @log_calls # Добавляем логирование
    def get_confirmation_message(self):
        return self.get_text(self.CONFIRMATION_MESSAGE_LOCATOR)

    @log_calls # Добавляем логирование
    def get_sub_message(self):
        return self.get_text(self.SUB_MESSAGE_LOCATOR)

    @log_calls # Добавляем логирование
    def click_back_home(self):
        self.click(self.BACK_HOME_BUTTON)
