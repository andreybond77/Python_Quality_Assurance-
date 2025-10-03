def common_elements(list1, list2):
    """
    Функция принимает два списка чисел и возвращает список чисел,
    которые есть в обоих списках.

    Args:
        list1: Первый список чисел
        list2: Второй список чисел

    Returns:
        Список чисел, которые есть в обоих списках (без дубликатов)
    """
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Оба аргумента должны быть списками")

    for item in list1:
        if not isinstance(item, (int, float)):
            raise TypeError("Все элементы первого списка должны быть числами")

    for item in list2:
        if not isinstance(item, (int, float)):
            raise TypeError("Все элементы второго списка должны быть числами")

    # Находим пересечение множеств и возвращаем в виде списка
    set1 = set(list1)
    set2 = set(list2)
    common = set1.intersection(set2)

    # Возвращаем отсортированный список для предсказуемости
    return sorted(list(common))


def words_starting_with_vowel(text):
    """
    Функция принимает строку и возвращает список слов,
    которые начинаются на гласную букву.

    Args:
        text: Входная строка

    Returns:
        Список слов, начинающихся на гласную букву
    """
    if not isinstance(text, str):
        raise TypeError("Аргумент должен быть строкой")

    vowels = set('aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ')

    # Разбиваем строку на слова, убирая знаки препинания
    import re
    words = re.findall(r'\b\w+\b', text)

    # Фильтруем слова, которые начинаются на гласную
    result = []
    for word in words:
        if word and word[0] in vowels:
            result.append(word)

    return result