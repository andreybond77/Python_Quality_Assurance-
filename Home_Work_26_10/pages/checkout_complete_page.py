# checkout_complete_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CheckoutCompletePage(BasePage):
    """Page Object Model для страницы завершения оформления заказа."""

    # Локаторы элементов на странице checkout-complete
    TITLE_LOCATOR = (By.CLASS_NAME, "title") # Заголовок "Checkout: Complete!"
    CONFIRMATION_MESSAGE_LOCATOR = (By.CLASS_NAME, "complete-header") # Основное сообщение подтверждения
    SUB_MESSAGE_LOCATOR = (By.CLASS_NAME, "complete-text") # Дополнительный текст подтверждения
    BACK_HOME_BUTTON = (By.ID, "back-to-products") # Кнопка "Back Home"

    def __init__(self, driver):
        """Конструктор класса."""
        super().__init__(driver)

    def is_loaded(self):
        """Проверяет, загружена ли страница завершения оформления заказа."""
        try:
            # Ждем видимости заголовка "Checkout: Complete!"
            self.wait.until(EC.visibility_of_element_located(self.TITLE_LOCATOR))
            # Проверяем текст заголовка
            title_text = self.get_text(self.TITLE_LOCATOR)
            return title_text == "Checkout: Complete!"
        except:
            return False

    def get_page_title_text(self):
        """Получает текст заголовка страницы."""
        return self.get_text(self.TITLE_LOCATOR)

    def get_confirmation_message(self):
        """Получает основное сообщение подтверждения."""
        return self.get_text(self.CONFIRMATION_MESSAGE_LOCATOR)

    def get_sub_message(self):
        """Получает дополнительный текст подтверждения."""
        return self.get_text(self.SUB_MESSAGE_LOCATOR)

    def click_back_home(self):
        """Кликает по кнопке 'Back Home'."""
        self.click(self.BACK_HOME_BUTTON)
