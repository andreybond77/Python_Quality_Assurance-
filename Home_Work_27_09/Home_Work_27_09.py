class Converter:
    """Класс для конвертации различных единиц измерения"""

    @staticmethod
    def celsius_to_fahrenheit(c):
        """
        Перевод из градусов Цельсия в градусы Фаренгейта
        Формула: °F = °C * 9/5 + 32
        """
        if not isinstance(c, (int, float)):
            raise TypeError("Температура должна быть числом")
        return c * 9 / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        """
        Перевод из градусов Фаренгейта в градусы Цельсия
        Формула: °C = (°F - 32) * 5/9
        """
        if not isinstance(f, (int, float)):
            raise TypeError("Температура должна быть числом")
        return (f - 32) * 5 / 9

    @staticmethod
    def kilometers_to_miles(km):
        """
        Перевод из километров в мили
        Формула: мили = километры * 0.621371
        """
        if not isinstance(km, (int, float)):
            raise TypeError("Расстояние должно быть числом")
        if km < 0:
            raise ValueError("Расстояние не может быть отрицательным")
        return km * 0.621371

    @staticmethod
    def miles_to_kilometers(mi):
        """
        Перевод из миль в километры
        Формула: километры = мили / 0.621371
        """
        if not isinstance(mi, (int, float)):
            raise TypeError("Расстояние должно быть числом")
        if mi < 0:
            raise ValueError("Расстояние не может быть отрицательным")
        return mi / 0.621371