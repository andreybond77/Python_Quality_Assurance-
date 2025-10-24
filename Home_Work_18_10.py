# test_login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_with_waits():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)  # Явное ожидание на 10 секунд

    # --- Неявное ожидание ---
    driver.implicitly_wait(5)  # Неявное ожидание на 5 секунд (ждать все элементы до 5 сек)

    try:
        # 1. Открытие страницы логина
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # 2. Дождаться, пока элемент логина станет кликабельным (или видимым)
        username_input = wait.until(
            EC.element_to_be_clickable((By.NAME, "username"))
        )
        username_input.send_keys("Admin")

        # 3. Дождаться, пока элемент пароля станет кликабельным
        password_input = wait.until(
            EC.element_to_be_clickable((By.NAME, "password"))
        )
        password_input.send_keys("admin124")

        # 4. Дождаться, пока кнопка Login станет кликабельной
        login_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        login_button.click()

        # 5. После логина дождаться появления элемента на главной странице (например, заголовка)
        dashboard_header = wait.until(
            EC.presence_of_element_located((By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']"))
        )
        print("Успешный вход в систему. Заголовок:", dashboard_header.text)

    except Exception as e:
        print("Произошла ошибка:", e)
        driver.save_screenshot("error_screenshot.png") # Сделать скриншот при ошибке

    finally:
        # 6. Закрытие браузера
        driver.quit()

# Запуск теста
if __name__ == "__main__":
    test_login_with_waits()