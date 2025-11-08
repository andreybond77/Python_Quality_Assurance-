class InsufficientAmount(Exception):
    pass

class Wallet:
    usd_rate = 64  # Курс доллара к рублю

    def __init__(self, balance=0):
        self.__balance = balance  # Баланс в рублях
        self.__balance_usd = self.__calculate_usd_balance()

    def __calculate_usd_balance(self):
        return self.__balance / Wallet.usd_rate

    def get_balance(self):
        return self.__balance

    def get_balance_usd(self):
        # Расчитываем долларовый баланс по текущему курсу
        return self.__calculate_usd_balance()

    def add_cash(self, amount):
        self.__balance += amount
        print("Баланс карты: ", self.__balance)

    def spend_cash(self, spend_sum):
        if spend_sum <= self.__balance:
            self.__balance -= spend_sum
            print("Баланс карты: ", self.__balance)
        else:
            raise InsufficientAmount("Недостаточно средств на счету.")

