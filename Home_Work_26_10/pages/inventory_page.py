# pages.inventory_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    """Страница каталога товаров"""

    def add_to_cart(self, product_name):
        button = (By.XPATH,
                  f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
        self.click(button)

    def get_cart_count(self):
        count = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        return int(count)