# tests.test_inventory.py
import pytest
from conftest import *
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import log_calls # Импортируем декоратор

@log_calls # Добавляем логирование к тесту
def test_add_product(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.add_to_cart("Sauce Labs Fleece Jacket")

    assert inventory_page.get_cart_count() == 2