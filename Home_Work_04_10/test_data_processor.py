import pytest
from data_processor import clean_and_split, find_common_elements, format_name


class TestCleanAndSplit:
    def test_clean_and_split_normal(self):
        """Тестирует нормальный случай."""
        result = clean_and_split("  Apple, Banana, Cherry  ")
        expected = ["apple", "banana", "cherry"]
        assert result == expected

    def test_clean_and_split_empty_string(self):
        """Тестирует пустую строку."""
        result = clean_and_split("")
        expected = []
        assert result == expected

    def test_clean_and_split_none(self):
        """Тестирует случай, когда передано None."""
        result = clean_and_split(None)
        expected = []
        assert result == expected

    def test_clean_and_split_no_comma(self):
        """Тестирует строку без запятой."""
        result = clean_and_split("apple")
        expected = ["apple"]
        assert result == expected

    def test_clean_and_split_extra_spaces(self):
        """Тестирует строку с лишними пробелами."""
        result = clean_and_split("  apple , banana  , cherry  ")
        expected = ["apple ", " banana", " cherry"]  # пробелы до/после запятой остаются
        assert result == expected


class TestFindCommonElements:
    def test_find_common_elements_basic(self):
        """Тестирует базовый случай."""
        list1 = ["a", "b", "c"]
        list2 = ["b", "c", "d"]
        result = find_common_elements(list1, list2)
        expected = ["b", "c"]
        assert result == expected

    def test_find_common_elements_with_duplicates_in_list1(self):
        """Дубликаты в list1 дублируются в результате."""
        list1 = ["a", "b", "b", "c"]
        list2 = ["b", "c", "d"]
        result = find_common_elements(list1, list2)
        expected = ["b", "b", "c"]  # текущая логика позволяет дубликаты
        assert result == expected

    def test_find_common_elements_limited_by_10(self):
        """Тестирует, что учитывается только первые 10 элементов list2."""
        list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
        list2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
        result = find_common_elements(list1, list2)
        expected = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        assert result == expected

    def test_find_common_elements_empty_lists(self):
        """Тестирует оба списка пустые."""
        result = find_common_elements([], [])
        expected = []
        assert result == expected

    def test_find_common_elements_one_empty(self):
        """Тестирует один из списков пуст."""
        result = find_common_elements(["a"], [])
        expected = []
        assert result == expected

    def test_find_common_elements_no_common(self):
        """Тестирует, когда нет общих элементов."""
        result = find_common_elements(["a"], ["b"])
        expected = []
        assert result == expected


class TestFormatName:
    def test_format_name_with_middle_name(self):
        """Тестирует формат с отчеством."""
        result = format_name("иван", "иванов", "иванович")
        expected = "Иванов И. И."  # исправлено: добавлены точки
        assert result == expected

    def test_format_name_without_middle_name(self):
        """Тестирует формат без отчества."""
        result = format_name("иван", "иванов")
        expected = "Иванов И."  # исправлено: добавлена точка
        assert result == expected

    def test_format_name_empty_first_name(self):
        """Тестирует пустое имя."""
        result = format_name("", "иванов")
        expected = None
        assert result == expected

    def test_format_name_empty_last_name(self):
        """Тестирует пустую фамилию."""
        result = format_name("иван", "")
        expected = None
        assert result == expected

    def test_format_name_empty_middle_name(self):
        """Тестирует пустое отчество — как если бы его не было."""
        result = format_name("иван", "иванов", "")
        expected = "Иванов И."
        assert result == expected

    def test_format_name_all_caps(self):
        """Тестирует, что инициалы и фамилия правильно форматируются."""
        result = format_name("АЛЕКСАНДР", "ПОПОВ", "СЕРГЕЕВИЧ")
        expected = "Попов А. С."
        assert result == expected

    def test_format_name_single_char(self):
        """Тестирует однобуквенные имена."""
        result = format_name("А", "Б", "В")
        expected = "Б А. В."
        assert result == expected