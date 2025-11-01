# tests/test_checkout_process.py
import pytest
from conftest import * # Импорт фикстур из conftest.py
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page_one import CheckoutPageOne
from pages.checkout_page_two import CheckoutPageTwo
from pages.checkout_complete_page import CheckoutCompletePage

def test_checkout_process(driver):
    """
    Тест: Полный сценарий оформления заказа.
    Логин -> Добавление товара в корзину -> Переход в корзину -> Проверка содержимого ->
    Нажатие 'Checkout' -> Заполнение информации -> Нажатие 'Continue' ->
    Проверка содержимого заказа -> Нажатие 'Finish' -> Проверка подтверждения.
    """
    # 1. Инициализация POM
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page_one = CheckoutPageOne(driver)
    checkout_page_two = CheckoutPageTwo(driver)
    checkout_complete_page = CheckoutCompletePage(driver)

    # 2. Открытие страницы логина и логин
    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")

    # 3. Добавление товара в корзину (например, "Sauce Labs Bolt T-Shirt")
    PRODUCT_NAME = "Sauce Labs Bolt T-Shirt"
    inventory_page.add_to_cart(PRODUCT_NAME)

    # 4. Переход в корзину
    inventory_page.click_shopping_cart()

    # 5. Проверка содержимого корзины (ожидаем 1 товар)
    assert cart_page.get_cart_items_count() == 1, f"Ожидался 1 товар в корзине, найдено: {cart_page.get_cart_items_count()}"
    first_item_details = cart_page.get_cart_item_details(0)
    assert first_item_details["name"] == PRODUCT_NAME, f"Ожидалось имя товара '{PRODUCT_NAME}', получено: '{first_item_details['name']}'"

    # 6. Нажатие 'Checkout'
    cart_page.click_checkout()

    # 7. Проверка, что страница шага 1 загружена
    assert checkout_page_one.is_loaded(), "Страница 'Checkout: Your Information' не загрузилась"
    assert checkout_page_one.get_page_title_text() == "Checkout: Your Information", "Неверный заголовок страницы шага 1"

    # 8. Заполнение информации о покупателе
    checkout_page_one.fill_customer_info("John", "Doe", "12345")

    # 9. Нажатие 'Continue'
    checkout_page_one.click_continue()

    # 10. Проверка, что страница шага 2 загружена
    assert checkout_page_two.is_loaded(), "Страница 'Checkout: Overview' не загрузилась"
    assert checkout_page_two.get_page_title_text() == "Checkout: Overview", "Неверный заголовок страницы шага 2"

    # 11. Проверка содержимого заказа на шаге 2 (ожидаем 1 товар, тот же)
    assert checkout_page_two.get_cart_items_count() == 1, f"Ожидался 1 товар в заказе, найдено: {checkout_page_two.get_cart_items_count()}"
    overview_item_details = checkout_page_two.get_cart_item_details(0)
    assert overview_item_details["name"] == PRODUCT_NAME, f"Ожидалось имя товара '{PRODUCT_NAME}' в обзоре, получено: '{overview_item_details['name']}'"

    # 12. Нажатие 'Finish'
    checkout_page_two.click_finish()

    # 13. Проверка, что страница завершения загружена
    assert checkout_complete_page.is_loaded(), "Страница 'Checkout: Complete!' не загрузилась"
    assert checkout_complete_page.get_page_title_text() == "Checkout: Complete!", "Неверный заголовок страницы завершения"

    # 14. Проверка подтверждения
    confirmation_message = checkout_complete_page.get_confirmation_message()
    assert "Thank you for your order!" in confirmation_message, f"Ожидалось сообщение 'Thank you for your order!', получено: '{confirmation_message}'"

    print("Тест полного процесса оформления заказа пройден успешно.")
