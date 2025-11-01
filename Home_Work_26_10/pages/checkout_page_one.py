# checkout_page_one.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CheckoutPageOne(BasePage):
    """Page Object Model для страницы оформления заказа - Шаг 1 (Информация о покупателе)."""

    # Локаторы элементов на странице checkout-step-one
    TITLE_LOCATOR = (By.CLASS_NAME, "title") # Заголовок "Checkout: Your Information"
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.CLASS_NAME, "cart_cancel_link") # Кнопка "Cancel" ведет обратно в корзину

    def __init__(self, driver):
        """Конструктор класса."""
        super().__init__(driver)

    def is_loaded(self):
        """Проверяет, загружена ли страница шага 1 оформления заказа."""
        try:
            # Ждем видимости заголовка "Checkout: Your Information"
            self.wait.until(EC.visibility_of_element_located(self.TITLE_LOCATOR))
            # Проверяем текст заголовка
            title_text = self.get_text(self.TITLE_LOCATOR)
            return title_text == "Checkout: Your Information"
        except:
            return False

    def get_page_title_text(self):
        """Получает текст заголовка страницы."""
        return self.get_text(self.TITLE_LOCATOR)

    def fill_customer_info(self, first_name, last_name, postal_code):
        """Заполняет поля информации о покупателе."""
        self.type(self.FIRST_NAME_INPUT, first_name)
        self.type(self.LAST_NAME_INPUT, last_name)
        self.type(self.POSTAL_CODE_INPUT, postal_code)

    def click_continue(self):
        """Кликает по кнопке 'Continue'."""
        self.click(self.CONTINUE_BUTTON)

    def click_cancel(self):
        """Кликает по кнопке 'Cancel'."""
        self.click(self.CANCEL_BUTTON)
