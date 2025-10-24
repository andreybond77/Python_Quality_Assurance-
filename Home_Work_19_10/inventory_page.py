# inventory_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    """
    Page Object Model для страницы товаров (инвентаря).
    Предполагается, что пользователь уже авторизован и находится на странице инвентаря.
    URL: https://www.saucedemo.com/inventory.html (или https://www.saucedemo.com/v1/inventory.html)
    """

    def __init__(self, driver):
        """
        Конструктор класса.
        :param driver: Экземпляр WebDriver.
        """
        self.driver = driver
        # self.url = "https://www.saucedemo.com/inventory.html" # Убираем, POM не отвечает за открытие
        self.wait = WebDriverWait(driver, 10)

        # Локаторы элементов на странице инвентаря
        # Локатор заголовка "Products" на странице инвентаря
        self.title_locator = (By.CLASS_NAME, "title")
        # Локатор для добавления конкретного товара (например, "Sauce Labs Bolt T-Shirt")
        # ID кнопки add-to-cart для "Sauce Labs Bolt T-Shirt" на v1
        self.add_to_cart_bolt_tshirt_locator = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        # Локатор ссылки на корзину
        self.shopping_cart_link_locator = (By.CLASS_NAME, "shopping_cart_link")


    # def open(self): # Убираем метод open
    #     self.driver.get(self.url)


    def is_loaded(self):
        """
        Проверяет, загружена ли страница инвентаря.
        Ожидает видимость заголовка 'Products'.
        :return: True, если страница загружена, иначе False.
        """
        try:
            # Ждем, пока элемент с классом 'title' станет видимым
            self.wait.until(EC.visibility_of_element_located(self.title_locator))
            # Проверяем, что текст элемента - 'Products'
            title_element = self.driver.find_element(*self.title_locator)
            return title_element.text == "Products"
        except:
            return False


    def get_page_title_text(self):
        """
        Получает текст заголовка на странице инвентаря.
        :return: Текст заголовка (например, 'Products').
        """
        title_element = self.wait.until(EC.visibility_of_element_located(self.title_locator))
        return title_element.text


    def add_bolt_tshirt_to_cart(self):
        """
        Находит товар 'Sauce Labs Bolt T-Shirt' и добавляет его в корзину.
        """
        # Ждем, пока кнопка 'ADD TO CART' для конкретного товара станет кликабельной
        add_button = self.wait.until(EC.element_to_be_clickable(self.add_to_cart_bolt_tshirt_locator))
        add_button.click()


    def click_shopping_cart(self):
        """
        Кликает по иконке/ссылке корзины.
        """
        # Ждем, пока ссылка на корзину станет кликабельной
        cart_link = self.wait.until(EC.element_to_be_clickable(self.shopping_cart_link_locator))
        cart_link.click()
