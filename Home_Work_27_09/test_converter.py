import unittest
from Home_Work_27_09 import Converter


class TestConverter(unittest.TestCase):
    """Тесты для класса Converter"""

    def setUp(self):
        """Установка тестового окружения"""
        self.converter = Converter()

    def test_celsius_to_fahrenheit_positive(self):
        """Тест конвертации из Цельсия в Фаренгейт (положительные значения)"""
        self.assertEqual(self.converter.celsius_to_fahrenheit(0), 32)
        self.assertEqual(self.converter.celsius_to_fahrenheit(100), 212)
        self.assertAlmostEqual(self.converter.celsius_to_fahrenheit(37), 98.6, places=1)
        self.assertAlmostEqual(self.converter.celsius_to_fahrenheit(25), 77)

    def test_celsius_to_fahrenheit_negative(self):
        """Тест конвертации из Цельсия в Фаренгейт (отрицательные значения)"""
        self.assertEqual(self.converter.celsius_to_fahrenheit(-40), -40)
        self.assertEqual(self.converter.celsius_to_fahrenheit(-10), 14)

    def test_celsius_to_fahrenheit_fractional(self):
        """Тест конвертации из Цельсия в Фаренгейт (дробные значения)"""
        self.assertAlmostEqual(self.converter.celsius_to_fahrenheit(0.5), 32.9)
        self.assertAlmostEqual(self.converter.celsius_to_fahrenheit(-5.5), 22.1)

    def test_fahrenheit_to_celsius_positive(self):
        """Тест конвертации из Фаренгейта в Цельсий (положительные значения)"""
        self.assertEqual(self.converter.fahrenheit_to_celsius(32), 0)
        self.assertEqual(self.converter.fahrenheit_to_celsius(212), 100)
        self.assertAlmostEqual(self.converter.fahrenheit_to_celsius(98.6), 37, places=1)
        self.assertAlmostEqual(self.converter.fahrenheit_to_celsius(77), 25)

    def test_fahrenheit_to_celsius_negative(self):
        """Тест конвертации из Фаренгейта в Цельсий (отрицательные значения)"""
        self.assertEqual(self.converter.fahrenheit_to_celsius(-40), -40)
        self.assertEqual(self.converter.fahrenheit_to_celsius(14), -10)

    def test_fahrenheit_to_celsius_fractional(self):
        """Тест конвертации из Фаренгейта в Цельсий (дробные значения)"""
        self.assertAlmostEqual(self.converter.fahrenheit_to_celsius(32.9), 0.5)
        self.assertAlmostEqual(self.converter.fahrenheit_to_celsius(22.1), -5.5)

    def test_kilometers_to_miles_positive(self):
        """Тест конвертации из километров в мили (положительные значения)"""
        self.assertAlmostEqual(self.converter.kilometers_to_miles(1), 0.621371, places=6)
        self.assertAlmostEqual(self.converter.kilometers_to_miles(10), 6.21371, places=5)
        self.assertAlmostEqual(self.converter.kilometers_to_miles(100), 62.1371, places=4)

    def test_kilometers_to_miles_zero(self):
        """Тест конвертации из километров в мили (нулевое значение)"""
        self.assertEqual(self.converter.kilometers_to_miles(0), 0)

    def test_miles_to_kilometers_positive(self):
        """Тест конвертации из миль в километры (положительные значения)"""
        self.assertAlmostEqual(self.converter.miles_to_kilometers(1), 1.609344, places=6)
        self.assertAlmostEqual(self.converter.miles_to_kilometers(5), 8.04672, places=5)
        self.assertAlmostEqual(self.converter.miles_to_kilometers(10), 16.09344, places=5)

    def test_miles_to_kilometers_zero(self):
        """Тест конвертации из миль в километры (нулевое значение)"""
        self.assertEqual(self.converter.miles_to_kilometers(0), 0)

    def test_round_trip_conversion(self):
        """Тест обратного преобразования (точность)"""
        celsius = 25
        fahrenheit = self.converter.celsius_to_fahrenheit(celsius)
        back_to_celsius = self.converter.fahrenheit_to_celsius(fahrenheit)
        self.assertAlmostEqual(celsius, back_to_celsius, places=5)

    def test_kilometers_negative_value(self):
        """Тест отрицательного значения для километров"""
        with self.assertRaises(ValueError):
            self.converter.kilometers_to_miles(-10)

    def test_miles_negative_value(self):
        """Тест отрицательного значения для миль"""
        with self.assertRaises(ValueError):
            self.converter.miles_to_kilometers(-5)

    def test_invalid_input_type_celsius_to_fahrenheit(self):
        """Тест недопустимого типа ввода для celsius_to_fahrenheit"""
        with self.assertRaises(TypeError):
            self.converter.celsius_to_fahrenheit("invalid")
        with self.assertRaises(TypeError):
            self.converter.celsius_to_fahrenheit(None)
        with self.assertRaises(TypeError):
            self.converter.celsius_to_fahrenheit([])

    def test_invalid_input_type_fahrenheit_to_celsius(self):
        """Тест недопустимого типа ввода для fahrenheit_to_celsius"""
        with self.assertRaises(TypeError):
            self.converter.fahrenheit_to_celsius("invalid")
        with self.assertRaises(TypeError):
            self.converter.fahrenheit_to_celsius(None)
        with self.assertRaises(TypeError):
            self.converter.fahrenheit_to_celsius({})

    def test_invalid_input_type_kilometers_to_miles(self):
        """Тест недопустимого типа ввода для kilometers_to_miles"""
        with self.assertRaises(TypeError):
            self.converter.kilometers_to_miles("invalid")
        with self.assertRaises(TypeError):
            self.converter.kilometers_to_miles(None)
        with self.assertRaises(TypeError):
            self.converter.kilometers_to_miles(())

    def test_invalid_input_type_miles_to_kilometers(self):
        """Тест недопустимого типа ввода для miles_to_kilometers"""
        with self.assertRaises(TypeError):
            self.converter.miles_to_kilometers("invalid")
        with self.assertRaises(TypeError):
            self.converter.miles_to_kilometers(None)
        with self.assertRaises(TypeError):
            self.converter.miles_to_kilometers(set())


if __name__ == '__main__':
    unittest.main()