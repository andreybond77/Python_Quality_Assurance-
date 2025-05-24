# 5. Задача о числах Фибоначчи:
# Напишите программу, которая выводит первые 10 чисел
# Фибоначчи.
# 6. Задача о выводе чисел в обратном порядке:
# Напишите программу, которая выводит числа от 10 до 1
# в обратном порядке.
# 7. Задача о подсчете гласных букв:
# Напишите программу, которая считает количество
# гласных букв в заданной строке.
# 8. Задача о сумме цифр числа: Напишите программу,
# которая считает сумму цифр заданного числа.
# 9. Задача о выводе таблицы умножения:
# Напишите программу, которая выводит таблицу
# умножения от 1 до 10.
# Сделайте commit и push в ваш репозиторий
# Результат работы: ссылка на ваш репозиторий в github

# def fibonacci(n):
#     fib_sequence = []
#     a, b = 0, 1
#     for _ in range(n):
#         fib_sequence.append(a)
#         a, b = b, a + b
#     return fib_sequence
#
# # Выводим первые 10 чисел Фибоначчи
# first_10_fibonacci = fibonacci(10)
# print(first_10_fibonacci)

################################################

# def print_numbers_reverse(start, end):
#     for number in range(start, end - 1, -1):
#         print(number)
#
# # Выводим числа от 10 до 1 в обратном порядке
# print_numbers_reverse(10, 1)

###################################################

# def count_vowels(input_string):
#     vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"  # Гласные буквы русского алфавита
#     count = 0
#     for char in input_string:
#         if char in vowels:
#             count += 1
#     return count
#
# # Пример использования
# input_string = input("Введите строку: ")
# vowel_count = count_vowels(input_string)
# print(f"Количество гласных букв: {vowel_count}")

############################################################

# def sum_of_digits(number):
#     total = 0
#     for digit in str(number):
#         total += int(digit)
#     return total
#
# # Пример использования
# input_number = input("Введите число: ")
# digit_sum = sum_of_digits(input_number)
# print(f"Сумма цифр числа {input_number}: {digit_sum}")

##########################################################################

def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print()  # Пустая строка для разделения таблиц

# Выводим таблицу умножения
multiplication_table()









