# tests/test_checkout_process.py
import pytest
from conftest import *
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page_one import CheckoutPageOne
from pages.checkout_page_two import CheckoutPageTwo
from pages.checkout_complete_page import CheckoutCompletePage
from utils.logger import log_calls # Импортируем декоратор

@log_calls # Добавляем логирование к тесту
def test_checkout_process(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page_one = CheckoutPageOne(driver)
    checkout_page_two = CheckoutPageTwo(driver)
    checkout_complete_page = CheckoutCompletePage(driver)

    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")

    PRODUCT_NAME = "Sauce Labs Bolt T-Shirt"
    inventory_page.add_to_cart(PRODUCT_NAME)

    inventory_page.click_shopping_cart()

    assert cart_page.get_cart_items_count() == 1, f"Ожидался 1 товар в корзине, найдено: {cart_page.get_cart_items_count()}"
    first_item_details = cart_page.get_cart_item_details(0)
    assert first_item_details["name"] == PRODUCT_NAME, f"Ожидалось имя товара '{PRODUCT_NAME}', получено: '{first_item_details['name']}'"

    cart_page.click_checkout()

    assert checkout_page_one.is_loaded(), "Страница 'Checkout: Your Information' не загрузилась"
    assert checkout_page_one.get_page_title_text() == "Checkout: Your Information", "Неверный заголовок страницы шага 1"

    checkout_page_one.fill_customer_info("John", "Doe", "12345")
    checkout_page_one.click_continue()

    assert checkout_page_two.is_loaded(), "Страница 'Checkout: Overview' не загрузилась"
    assert checkout_page_two.get_page_title_text() == "Checkout: Overview", "Неверный заголовок страницы шага 2"

    assert checkout_page_two.get_cart_items_count() == 1, f"Ожидался 1 товар в заказе, найдено: {checkout_page_two.get_cart_items_count()}"
    overview_item_details = checkout_page_two.get_cart_item_details(0)
    assert overview_item_details["name"] == PRODUCT_NAME, f"Ожидалось имя товара '{PRODUCT_NAME}' в обзоре, получено: '{overview_item_details['name']}'"

    checkout_page_two.click_finish()

    assert checkout_complete_page.is_loaded(), "Страница 'Checkout: Complete!' не загрузилась"
    assert checkout_complete_page.get_page_title_text() == "Checkout: Complete!", "Неверный заголовок страницы завершения"

    confirmation_message = checkout_complete_page.get_confirmation_message()
    assert "Thank you for your order!" in confirmation_message, f"Ожидалось сообщение 'Thank you for your order!', получено: '{confirmation_message}'"

    print("Тест полного процесса оформления заказа пройден успешно.")
