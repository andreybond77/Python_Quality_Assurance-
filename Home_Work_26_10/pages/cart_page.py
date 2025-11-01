# cart_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CartPage(BasePage):
    """Page Object Model для страницы корзины."""

    # Локаторы элементов на странице корзины
    # Заголовок страницы "Your Cart"
    TITLE_LOCATOR = (By.CLASS_NAME, "title")
    # Кнопка "Checkout"
    CHECKOUT_BUTTON_LOCATOR = (By.ID, "checkout")
    # Кнопка "Continue Shopping" (не обязательна для основного сценария)
    CONTINUE_SHOPPING_BUTTON_LOCATOR = (By.NAME, "continue-shopping")
    # Кнопка "Remove" для товара (обычно появляется для каждого товара)
    # Для упрощения, будем искать первую кнопку "Remove"
    REMOVE_BUTTON_LOCATOR = (By.CLASS_NAME, "btn_secondary") # Класс для кнопки "Remove"
    # Элементы, представляющие каждый товар в корзине (их контейнеры)
    CART_ITEM_LOCATORS = (By.CLASS_NAME, "cart_item")
    # Элемент с названием товара внутри контейнера
    ITEM_NAME_LOCATOR = (By.CLASS_NAME, "inventory_item_name")
    # Элемент с описанием товара внутри контейнера
    ITEM_DESC_LOCATOR = (By.CLASS_NAME, "inventory_item_desc")
    # Элемент с ценой товара внутри контейнера
    ITEM_PRICE_LOCATOR = (By.CLASS_NAME, "inventory_item_price")

    def __init__(self, driver):
        """Конструктор класса."""
        super().__init__(driver)

    def is_loaded(self):
        """Проверяет, загружена ли страница корзины."""
        try:
            # Ждем видимости заголовка "Your Cart"
            self.wait.until(EC.visibility_of_element_located(self.TITLE_LOCATOR))
            # Проверяем текст заголовка
            title_text = self.get_text(self.TITLE_LOCATOR)
            return title_text == "Your Cart"
        except:
            return False

    def get_page_title_text(self):
        """Получает текст заголовка страницы корзины."""
        return self.get_text(self.TITLE_LOCATOR)

    def click_checkout(self):
        """Кликает по кнопке 'Checkout'."""
        self.click(self.CHECKOUT_BUTTON_LOCATOR)

    def click_continue_shopping(self):
        """Кликает по кнопке 'Continue Shopping'."""
        self.click(self.CONTINUE_SHOPPING_BUTTON_LOCATOR)

    def click_remove_first_item(self):
        """Кликает по кнопке 'Remove' первого товара в корзине."""
        # Ждем, пока хотя бы один элемент корзины появится
        self.wait.until(EC.presence_of_element_located(self.CART_ITEM_LOCATORS))
        # Находим первую кнопку "Remove" и кликаем
        remove_button = self.driver.find_element(*self.REMOVE_BUTTON_LOCATOR)
        remove_button.click()

    def get_cart_items_count(self):
        """Возвращает количество товаров в корзине."""
        items = self.wait.until(EC.presence_of_all_elements_located(self.CART_ITEM_LOCATORS))
        return len(items)

    def get_cart_item_details(self, index=0):
        """
        Возвращает детали конкретного товара в корзине по индексу.
        :param index: Индекс товара (по умолчанию 0 - первый товар).
        :return: Словарь с ключами 'name', 'description', 'price'.
        """
        # Ждем, пока элементы корзины появятся
        items = self.wait.until(EC.presence_of_all_elements_located(self.CART_ITEM_LOCATORS))

        if index >= len(items):
            raise IndexError(f"Индекс {index} превышает количество товаров в корзине ({len(items)}).")

        item_element = items[index]
        # Находим элементы внутри конкретного товара
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
        Возвращает список словарей с деталями всех товаров в корзине.
        :return: Список словарей, каждый из которых содержит 'name', 'description', 'price'.
        """
        # Ждем, пока элементы корзины появятся
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
