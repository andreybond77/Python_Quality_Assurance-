import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


@pytest.fixture
def driver():
    options = Options()
    # options.add_argument("--headless")  # Убираем headless, чтобы видеть, что происходит
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_successful_checkout(driver):
    # 1. Вход в систему
    driver.get("https://www.saucedemo.com/")  # ✅ Убраны пробелы
    wait = WebDriverWait(driver, 10)

    # Правильные локаторы
    username_input = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    time.sleep(3)

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()

    time.sleep(3)
    #  Явное ожидание, пока текущий URL станет содержать "saucedemo.com"
    WebDriverWait(driver, 10).until(EC.url_contains("saucedemo.com"))

    # Проверка успешной перезагрузки страницы
    assert "saucedemo.com" in driver.current_url, "Не удалось перейти на saucedemo.com"

    #  Добавление товара (например, "Sauce Labs Backpack")
    backpack_add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack" )
    backpack_add_button.click()

    time.sleep(3)

    #  Переход в корзину — явно переходим по URL
    basket_button = driver.find_element(By.ID, "shopping_cart_container")
    basket_button.click()

    # Проверка успешной перезагрузки страницы
    assert "cart" in driver.current_url, "Не удалось перейти на cart"


    time.sleep(3)

    #  Проверка товара в корзине
    item_name = driver.find_element(By.ID,"item_4_title_link")
    assert "Sauce Labs Backpack" in item_name.text, "Товар не найден в корзине"


    #  Начало оформления заказа (ожидаем кнопку "Checkout")
    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    # Проверка успешной перезагрузки страницы
    assert "checkout-step-one" in driver.current_url, "Не удалось перейти на checkout-step-one"

    #  Ввод данных (ожидаем появления полей)
    first_name_input = driver.find_element(By.ID, "first-name")
    last_name_input = driver.find_element(By.ID, "last-name")
    postal_code_input = driver.find_element(By.ID, "postal-code")
    time.sleep(3)
    first_name_input.send_keys("Иван")
    last_name_input.send_keys("Иванов")
    postal_code_input.send_keys("12345")
    time.sleep(3)
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()
    time.sleep(3)

    #  Завершение заказа
    finish_button = driver.find_element(By.ID, "finish")
    finish_button.click()
    time.sleep(3)

    #  Проверка успешного завершения
    thank_you_message = driver.find_element(By.CLASS_NAME, "complete-header")
    assert "Thank you for your order!" in thank_you_message.text, "Заказ не был успешно оформлен"