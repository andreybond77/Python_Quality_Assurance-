# tests/test_cart_operations.py
import pytest
from conftest import *
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.logger import log_calls # Импортируем декоратор

@log_calls # Добавляем логирование к тесту
def test_add_and_remove_product_from_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")

    PRODUCT_NAME = "Sauce Labs Backpack"
    inventory_page.add_to_cart(PRODUCT_NAME)

    inventory_page.click_shopping_cart()

    assert cart_page.is_loaded(), "Страница корзины не загрузилась"
    assert cart_page.get_page_title_text() == "Your Cart", "Неверный заголовок страницы корзины"

    assert cart_page.get_cart_items_count() == 1, f"Ожидался 1 товар в корзине, найдено: {cart_page.get_cart_items_count()}"

    first_item_details = cart_page.get_cart_item_details(0)
    assert first_item_details["name"] == PRODUCT_NAME, f"Ожидалось имя товара '{PRODUCT_NAME}', получено: '{first_item_details['name']}'"

    cart_page.click_remove_first_item()

    # Ждем, пока элементы корзины исчезнут
    cart_page.wait.until(lambda d: len(d.find_elements(*CartPage.CART_ITEM_LOCATORS)) == 0)
    assert cart_page.get_cart_items_count() == 0, f"После удаления ожидалась пустая корзина (0 товаров), найдено: {cart_page.get_cart_items_count()}"

    print("Тест добавления и удаления товара из корзины пройден успешно.")
