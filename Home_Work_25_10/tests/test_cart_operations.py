# tests/test_cart_operations.py
import pytest
from conftest import * # Импорт фикстур из conftest.py
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_add_and_remove_product_from_cart(driver):
    """
    Тест: Добавление товара в корзину, проверка содержимого, удаление товара, проверка пустой корзины.
    """
    # 1. Инициализация POM
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    # 2. Открытие страницы логина и логин
    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")

    # 3. Добавление товара в корзину (например, "Sauce Labs Backpack")
    PRODUCT_NAME = "Sauce Labs Backpack"
    inventory_page.add_to_cart(PRODUCT_NAME)

    # 4. Переход в корзину
    inventory_page.click_shopping_cart() # Используем метод из InventoryPage для перехода

    # 5. Проверка, что страница корзины загружена
    assert cart_page.is_loaded(), "Страница корзины не загрузилась"
    assert cart_page.get_page_title_text() == "Your Cart", "Неверный заголовок страницы корзины"

    # 6. Проверка содержимого корзины (ожидаем 1 товар)
    assert cart_page.get_cart_items_count() == 1, f"Ожидался 1 товар в корзине, найдено: {cart_page.get_cart_items_count()}"

    # 7. Получение деталей первого товара и проверка его имени
    first_item_details = cart_page.get_cart_item_details(0) # Индекс 0 для первого товара
    assert first_item_details["name"] == PRODUCT_NAME, f"Ожидалось имя товара '{PRODUCT_NAME}', получено: '{first_item_details['name']}'"

    # 8. Удаление первого товара
    cart_page.click_remove_first_item()

    # 9. Проверка, что корзина пуста (ожидаем 0 товаров)
    cart_page.wait.until(lambda d: len(d.find_elements(*CartPage.CART_ITEM_LOCATORS)) == 0)
    assert cart_page.get_cart_items_count() == 0, f"После удаления ожидалась пустая корзина (0 товаров), найдено: {cart_page.get_cart_items_count()}"


    print("Тест добавления и удаления товара из корзины пройден успешно.")
