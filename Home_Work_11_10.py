import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = Options()
    # options.add_argument("--headless")  # Раскомментируйте для фоновом режима
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_example_page(driver):
    # 1. Открыть страницу
    driver.get("http://example.com")

    # 2. Явное ожидание для заголовка
    header = driver.find_element(By.TAG_NAME,"h1")
   # header = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))

    # Проверка текста элемента
    expected_text = "Example Domain"
    assert header.text == expected_text, f"Ожидали: {expected_text}, получили: {header.text}"

    # 3. Найти активную ссылку и кликнуть по ней
    link = driver.find_element(By.LINK_TEXT,"Learn more")
    link.click()

    # 4. Явное ожидание, пока текущий URL станет содержать "iana.org"
    WebDriverWait(driver, 10).until(EC.url_contains("iana.org"))

    # Проверка успешной перезагрузки страницы
    assert "iana.org" in driver.current_url, "Не удалось перейти на iana.org"