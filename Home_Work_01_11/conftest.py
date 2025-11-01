# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure
import os
import logging # Импортируем logging

# --- ЦЕНТРАЛИЗОВАННАЯ НАСТРОЙКА ЛОГИРОВАНИЯ ---
# Настройка корневого логгера или логгера проекта
logging.basicConfig(
    level=logging.INFO, # Уровень логирования
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', # Формат
    handlers=[
        logging.StreamHandler(), # Вывод в консоль
        # logging.FileHandler("project.log") # Опционально: вывод в файл
    ]
)

@pytest.fixture
def driver():
    """Фикстура для запуска и завершения браузера"""
    options = Options()
    options.add_argument("--start-maximized")
    prefs = {
        "profile.password_manager_leak_detection": False
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    yield driver

    if hasattr(driver, "get_screenshot_as_png"):
        allure.attach(driver.get_screenshot_as_png(),
                      name="screenshot",
                      attachment_type=allure.attachment_type.PNG)

    driver.quit()