# pages.checkout_page_two.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utils.logger import log_calls # Импортируем декоратор

class CheckoutPageTwo(BasePage):
    """Page Object Model для страницы оформления заказа - Шаг 2 (Обзор заказа)."""

    TITLE_LOCATOR = (By.CLASS_NAME, "title")
    FINISH_BUTTON = (By.ID, "finish")
    CANCEL_BUTTON = (By.CLASS_NAME, "cart_cancel_link")
    CART_ITEM_LOCATORS = (By.CLASS_NAME, "cart_item")
    ITEM_NAME_LOCATOR = (By.CLASS_NAME, "inventory_item_name")
    ITEM_DESC_LOCATOR = (By.CLASS_NAME, "inventory_item_desc")
    ITEM_PRICE_LOCATOR = (By.CLASS_NAME, "inventory_item_price")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    @log_calls # Добавляем логирование
    def is_loaded(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.TITLE_LOCATOR))
            title_text = self.get_text(self.TITLE_LOCATOR)
            return title_text == "Checkout: Overview"
        except:
            return False

    @log_calls # Добавляем логирование
    def get_page_title_text(self):
        return self.get_text(self.TITLE_LOCATOR)

    @log_calls # Добавляем логирование
    def click_finish(self):
        self.click(self.FINISH_BUTTON)

    @log_calls # Добавляем логирование
    def click_cancel(self):
        self.click(self.CANCEL_BUTTON)

    @log_calls # Добавляем логирование
    def get_cart_items_count(self):
        items = self.wait.until(EC.presence_of_all_elements_located(self.CART_ITEM_LOCATORS))
        return len(items)

    @log_calls # Добавляем логирование
    def get_cart_item_details(self, index=0):
        items = self.wait.until(EC.presence_of_all_elements_located(self.CART_ITEM_LOCATORS))
        if index >= len(items):
            raise IndexError(f"Индекс {index} превышает количество товаров в заказе ({len(items)}).")
        item_element = items[index]
        name_element = item_element.find_element(*self.ITEM_NAME_LOCATOR)
        desc_element = item_element.find_element(*self.ITEM_DESC_LOCATOR)
        price_element = item_element.find_element(*self.ITEM_PRICE_LOCATOR)
        return {
            "name": name_element.text,
            "description": desc_element.text,
            "price": price_element.text
        }

    @log_calls # Добавляем логирование
    def get_all_cart_items_details(self):
        items = self.wait.until(EC.presence_of_all_elements_located(self.CART_ITEM_LOCATORS))
        all_details = []
        for item_element in items:
            name_element = item_element.find_element(*self.ITEM_NAME_LOCATOR)
            desc_element = item_element.find_element(*self.ITEM_DESC_LOCATOR)
            price_element = item_element.find_element(*self.ITEM_PRICE_LOCATOR)
            all_details.append({
                "name": name_element.text,
                "description": desc_element.text,
                "price": price_element.text
            })
        return all_details

    @log_calls # Добавляем логирование
    def get_total_amount(self):
        total_element = self.wait.until(EC.presence_of_element_located(self.TOTAL_LABEL))
        return total_element.text
