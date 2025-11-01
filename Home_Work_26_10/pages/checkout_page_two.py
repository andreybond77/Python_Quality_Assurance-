# checkout_page_two.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CheckoutPageTwo(BasePage):
    """Page Object Model для страницы оформления заказа - Шаг 2 (Обзор заказа)."""

    # Локаторы элементов на странице checkout-step-two
    TITLE_LOCATOR = (By.CLASS_NAME, "title") # Заголовок "Checkout: Overview"
    FINISH_BUTTON = (By.ID, "finish")
    CANCEL_BUTTON = (By.CLASS_NAME, "cart_cancel_link") # Кнопка "Cancel" ведет обратно к шагу 1
    # Локаторы для проверки содержимого заказа (аналогично cart_page.py)
    CART_ITEM_LOCATORS = (By.CLASS_NAME, "cart_item")
    ITEM_NAME_LOCATOR = (By.CLASS_NAME, "inventory_item_name")
    ITEM_DESC_LOCATOR = (By.CLASS_NAME, "inventory_item_desc")
    ITEM_PRICE_LOCATOR = (By.CLASS_NAME, "inventory_item_price")
    # Локаторы для итоговой информации (итоговая цена, налог и т.д.)
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label") # Общий итог (Subtotal, Tax, Total)

    def __init__(self, driver):
        """Конструктор класса."""
        super().__init__(driver)

    def is_loaded(self):
        """Проверяет, загружена ли страница шага 2 оформления заказа."""
        try:
            # Ждем видимости заголовка "Checkout: Overview"
            self.wait.until(EC.visibility_of_element_located(self.TITLE_LOCATOR))
            # Проверяем текст заголовка
            title_text = self.get_text(self.TITLE_LOCATOR)
            return title_text == "Checkout: Overview"
        except:
            return False

    def get_page_title_text(self):
        """Получает текст заголовка страницы."""
        return self.get_text(self.TITLE_LOCATOR)

    def click_finish(self):
        """Кликает по кнопке 'Finish'."""
        self.click(self.FINISH_BUTTON)

    def click_cancel(self):
        """Кликает по кнопке 'Cancel'."""
        self.click(self.CANCEL_BUTTON)

    def get_cart_items_count(self):
        """Возвращает количество товаров в заказе."""
        items = self.wait.until(EC.presence_of_all_elements_located(self.CART_ITEM_LOCATORS))
        return len(items)

    def get_cart_item_details(self, index=0):
        """
        Возвращает детали конкретного товара в заказе по индексу.
        :param index: Индекс товара (по умолчанию 0 - первый товар).
        :return: Словарь с ключами 'name', 'description', 'price'.
        """
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

    def get_all_cart_items_details(self):
        """
        Возвращает список словарей с деталями всех товаров в заказе.
        :return: Список словарей, каждый из которых содержит 'name', 'description', 'price'.
        """
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

    def get_total_amount(self):
        """Получает текст итоговой суммы заказа."""
        # Ищем элемент с классом, содержащим итоговую сумму
        total_element = self.wait.until(EC.presence_of_element_located(self.TOTAL_LABEL))
        return total_element.text
