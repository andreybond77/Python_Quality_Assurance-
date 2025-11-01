# tests.test_login.py
import pytest
from conftest import *
from pages.login_page import LoginPage
from utils.logger import log_calls # Импортируем декоратор

@pytest.mark.ui
@pytest.mark.smoke
@log_calls # Добавляем логирование к тесту
def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")

@pytest.mark.ui
@pytest.mark.regression
@log_calls # Добавляем логирование к тесту
def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login("invalid", "wrong")

    error_text = login_page.get_error_message()
    assert "Epic sadface" in error_text, f"Ожидалось сообщение об ошибке, содержащее 'Epic sadface', получено: '{error_text}'"