# pages.inventory_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import log_calls # Импортируем декоратор

class InventoryPage(BasePage):
    """Страница каталога товаров"""

    CART_BADGE_LOCATOR = (By.CLASS_NAME, "shopping_cart_badge")

    @log_calls # Добавляем логирование
    def add_to_cart(self, product_name):
        button = (By.XPATH,
                  f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
        self.click(button)

    @log_calls # Добавляем логирование
    def get_cart_count(self):
        count_text = self.get_text(self.CART_BADGE_LOCATOR)
        return int(count_text)

    @log_calls # Добавляем логирование
    def click_shopping_cart(self):
        # Используем локатор бейджа корзины для клика, так как он кликабелен
        self.click(self.CART_BADGE_LOCATOR)