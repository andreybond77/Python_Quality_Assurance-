# test_inventory_with_pom.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from inventory_page import InventoryPage # Импортируем наш POM

@pytest.fixture
def driver():
    options = Options()
    # options.add_argument("--headless") # Раскомментируйте, если хотите запускать без GUI
    options.add_argument("--start-maximized")
    options.add_experimental_option("prefs", {
        "profile.password_manager_leak_detection": False
    })
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_add_bolt_tshirt_to_cart_pom(driver):
    """Тест добавления товара в корзину с использованием POM"""
    wait = WebDriverWait(driver, 10)

    # 1. Открыть страницу логина (https://www.saucedemo.com/)
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(5) # Неявное ожидание на 5 секунд

    # 2. Авторизация
    # Явное ожидание для полей ввода и кнопки
    username_input = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    username_input.send_keys("standard_user")

    password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password_input.send_keys("secret_sauce")

    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()

    # 3. Создаем экземпляр POM *после* авторизации
    inventory_page = InventoryPage(driver)

    # 4. Проверить, что страница инвентаря загружена (ожидаем, что мы на ней после логина)
    # Используем метод из POM
    assert inventory_page.is_loaded(), "Страница инвентаря не загрузилась или заголовок 'Products' не найден"
   

    # 5. Добавить товар в корзину
    inventory_page.add_bolt_tshirt_to_cart()

    # 6. Перейти в корзину и проверить товар
    inventory_page.click_shopping_cart()

    # Явное ожидание: ждем, пока элемент с названием товара (inventory_item_name) станет видимым на странице корзины
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name")))

    # Проверяем, что текст "Sauce Labs Bolt T-Shirt" присутствует в исходном коде страницы корзины
    assert "Sauce Labs Bolt T-Shirt" in driver.page_source, "Товар 'Sauce Labs Bolt T-Shirt' не найден в корзине"
