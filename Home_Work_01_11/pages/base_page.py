
# pages.base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from utils.logger import log_calls # Импортируем декоратор

class BasePage:
    """Базовый класс для всех страниц"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открываем страницу: {url}")
    @log_calls # Добавляем логирование
    def open(self, url):
        self.driver.get(url)

    @allure.step("Клик по элементу {locator}")
    @log_calls # Добавляем логирование
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Ввод текста '{text}' в поле {locator}")
    @log_calls # Добавляем логирование
    def type(self, locator, text):
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        elem.clear()
        elem.send_keys(text)

    @log_calls # Добавляем логирование
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text