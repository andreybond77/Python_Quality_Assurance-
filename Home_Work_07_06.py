def greet_and_count(user_name):
    # Удаляем пробелы из имени
    name_without_spaces = user_name.replace(" ", "")

    # Подсчитываем количество символов
    character_count = len(name_without_spaces)

    # Выводим приветствие
    print(f"Привет, {user_name}! Добро пожаловать!")

    # Выводим количество символов
    print(f"В твоем имени {character_count} символов (без учета пробелов).")


# Запрашиваем имя пользователя через терминал
user_input = input("Введите ваше имя: ")
greet_and_count(user_input)
