import pytest
from functions import common_elements, words_starting_with_vowel


class TestCommonElements:
    """Тесты для функции common_elements"""

    def test_common_elements_basic(self):
        """Тест основной функциональности"""
        assert common_elements([1, 2, 3], [3, 4, 5]) == [3]
        assert common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]

    def test_common_elements_empty_lists(self):
        """Тест с пустыми списками"""
        assert common_elements([], []) == []
        assert common_elements([1, 2, 3], []) == []
        assert common_elements([], [1, 2, 3]) == []

    def test_common_elements_no_common(self):
        """Тест когда нет общих элементов"""
        assert common_elements([1, 2, 3], [4, 5, 6]) == []

    def test_common_elements_duplicates(self):
        """Тест с дубликатами в списках"""
        assert common_elements([1, 2, 2, 3], [2, 2, 3, 4]) == [2, 3]
        assert common_elements([1, 1, 1], [1, 1, 1]) == [1]

    def test_common_elements_floats(self):
        """Тест с дробными числами"""
        assert common_elements([1.5, 2.0, 3.5], [2.0, 4.0, 5.0]) == [2.0]
        assert common_elements([1.1, 2.2, 3.3], [3.3, 4.4, 5.5]) == [3.3]

    def test_common_elements_mixed_numbers(self):
        """Тест с смешанными целыми и дробными числами"""
        assert common_elements([1, 2.0, 3], [2.0, 4, 5]) == [2.0]

    def test_common_elements_negative_numbers(self):
        """Тест с отрицательными числами"""
        assert common_elements([-1, -2, 3], [-2, 4, 5]) == [-2]
        assert common_elements([-1, -2, -3], [-3, -4, -5]) == [-3]

    def test_common_elements_identical_lists(self):
        """Тест с одинаковыми списками"""
        assert common_elements([1, 2, 3], [1, 2, 3]) == [1, 2, 3]

    def test_common_elements_single_element(self):
        """Тест с одиночными элементами"""
        assert common_elements([1], [1]) == [1]
        assert common_elements([1], [2]) == []

    def test_common_elements_type_error(self):
        """Тест на ошибки типов"""
        with pytest.raises(TypeError):
            common_elements("not a list", [1, 2, 3])

        with pytest.raises(TypeError):
            common_elements([1, 2, 3], "not a list")

        with pytest.raises(TypeError):
            common_elements([1, "not a number", 3], [1, 2, 3])

        with pytest.raises(TypeError):
            common_elements([1, 2, 3], [1, "not a number", 3])


class TestWordsStartingWithVowel:
    """Тесты для функции words_starting_with_vowel"""

    def test_basic_functionality(self):
        """Тест основной функциональности"""
        assert words_starting_with_vowel("apple banana orange grape") == ["apple", "orange"]
        assert words_starting_with_vowel("elephant tiger umbrella lion") == ["elephant", "umbrella"]

    def test_empty_string(self):
        """Тест с пустой строкой"""
        assert words_starting_with_vowel("") == []

    def test_no_vowel_words(self):
        """Тест когда нет слов на гласные"""
        assert words_starting_with_vowel("hello world python") == []

    def test_all_vowel_words(self):
        """Тест когда все слова на гласные"""
        assert words_starting_with_vowel("apple orange umbrella") == ["apple", "orange", "umbrella"]

    def test_mixed_case(self):
        """Тест с разным регистром"""
        assert words_starting_with_vowel("Apple banana ORANGE grape") == ["Apple", "ORANGE"]

    def test_punctuation(self):
        """Тест со знаками препинания"""
        assert words_starting_with_vowel("apple, banana; orange: grape!") == ["apple", "orange"]
        assert words_starting_with_vowel("Hello, (apple) and [orange]!") == ["apple", "orange"]

    def test_multiple_spaces(self):
        """Тест с несколькими пробелами"""
        assert words_starting_with_vowel("  apple   orange   banana  ") == ["apple", "orange"]

    def test_numbers_and_special_chars(self):
        """Тест с числами и специальными символами"""
        assert words_starting_with_vowel("apple123 banana orange456 grape") == ["apple123", "orange456"]
        assert words_starting_with_vowel("123 apple 456 orange") == ["apple", "orange"]

    def test_single_character_words(self):
        """Тест с однобуквенными словами"""
        assert words_starting_with_vowel("a b e c i d o f u g") == ["a", "e", "i", "o", "u"]

    def test_longer_words(self):
        """Тест с длинными словами"""
        assert words_starting_with_vowel("education programming innovation") == ["education", "innovation"]

    def test_russian_vowels(self):
        """Тест с русскими гласными"""
        assert words_starting_with_vowel("яблоко банан апельсин груша") == ["яблоко", "апельсин"]
        assert words_starting_with_vowel("ёжик медведь олень") == ["ёжик", "олень"]

    def test_type_error(self):
        """Тест на ошибки типов"""
        with pytest.raises(TypeError):
            words_starting_with_vowel(123)

        with pytest.raises(TypeError):
            words_starting_with_vowel(None)

        with pytest.raises(TypeError):
            words_starting_with_vowel([])

        with pytest.raises(TypeError):
            words_starting_with_vowel({})

    def test_capitalization_variations(self):
        """Тест с различными вариантами заглавных букв"""
        assert words_starting_with_vowel("Apple Banana Orange") == ["Apple", "Orange"]
        assert words_starting_with_vowel("APPLE BANANA ORANGE") == ["APPLE", "ORANGE"]
        assert words_starting_with_vowel("apple BANANA orange") == ["apple", "orange"]