import pytest
from wallet import Wallet, InsufficientAmount

@pytest.fixture()
def empty_wallet():
    """Создает пустой кошелек."""
    return Wallet()

@pytest.fixture()
def wallet():
    """Создает кошелек с начальными 100 рублями."""
    return Wallet(100)

def test_default_initial_amount(empty_wallet):
    """Проверяет, что начальный баланс пустого кошелька равен 0."""
    assert empty_wallet.get_balance() == 0

def test_setting_initial_amount(wallet):
    """Проверяет, что начальный баланс установленного кошелька равен 100."""
    assert wallet.get_balance() == 100

@pytest.mark.skip("bug #123")
def test_wallet_add_cash(wallet):
    """Проверяет добавление наличных в кошелек. Пропускается из-за ошибки."""
    wallet.add_cash(90)
    assert wallet.get_balance() == 190

def test_wallet_spend_cash(wallet):
    """Проверяет, что после списания 90 рублей остается 10 рублей."""
    wallet.spend_cash(90)
    assert wallet.get_balance() == 10

def test_wallet_spend_cash_exception(empty_wallet):
    """Проверяет, что выходит исключение при недостатке средств."""
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)

def test_wallet_initial_dollar_balance(empty_wallet):
    """Проверяет начальный баланс в долларах."""
    assert empty_wallet.get_balance_usd() == 0.0

def test_wallet_initial_dollar_balance_with_amount(wallet):
    """Проверяет начальный баланс в долларах для кошелька с начальными 100 рублями."""
    assert wallet.get_balance_usd() == 100 / Wallet.usd_rate  # Исправлено

def test_wallet_add_cash_updates_dollar_balance(wallet):
    """Проверяет, что добавление наличных обновляет баланс в долларах."""
    initial_usd_balance = wallet.get_balance_usd()
    wallet.add_cash(64)  # добавляем 64 рубля
    expected_usd_balance = (100 + 64) / Wallet.usd_rate  # Исправлено
    assert wallet.get_balance_usd() == expected_usd_balance

@pytest.mark.parametrize("earned, spend, expected", [
    (30, 10, 20),
    (20, 2, 18),
])
def test_transactions(earned, spend, expected, empty_wallet):
    """Проверяет правильность транзакций при зачислении и списании средств."""
    empty_wallet.add_cash(earned)
    empty_wallet.spend_cash(spend)
    assert empty_wallet.get_balance() == expected

