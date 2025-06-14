# def sort_three_numbers():
#     numbers = []
#     for i in range(3):
#         num = float(input(f"Введите число {i + 1}: "))
#         numbers.append(num)
#
#     numbers.sort()
#     print("Числа в порядке возрастания:", numbers)
#
#
# # Пример использования
# sort_three_numbers()

#########################################################

# def calculate_salary(sales):
#     base_salary = 200
#     if sales <= 500:
#         commission = sales * 0.03
#     elif sales <= 1000:
#         commission = sales * 0.05
#     else:
#         commission = sales * 0.08
#     return base_salary + commission
#
#
# def best_manager(salaries):
#     max_salary = max(salaries)
#     return salaries.index(max_salary)
#
#
# def main():
#     sales = []
#     for i in range(3):
#         sale = float(input(f"Введите уровень продаж для менеджера {i + 1}: "))
#         sales.append(sale)
#
#     salaries = [calculate_salary(sale) for sale in sales]
#
#     best_index = best_manager(salaries)
#     salaries[best_index] += 200  # Премия лучшему менеджеру
#
#     print("\nИтоги:")
#     for i in range(3):
#         print(f"Менеджер {i + 1}: Зарплата = {salaries[i]:.2f}$")
#     print(f"Лучший менеджер: Менеджер {best_index + 1} с зарплатой = {salaries[best_index]:.2f}$")
#
#
# # Пример использования
# main()

##########################################################

# def days_in_month(year,month):
#     if month in (1,3,5,7,8,10,10):
#         return 31
#     elif month in (4,6,9,11):
#         return 30
#     elif month == 2:
#         if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#             return  29
#         else:
#             return  28
#     else:
#         return "Некорректный месяц"
#
# def main():
#     year = int(input("Введите год: "))
#     month = int(input("Введите месяц (1-12): "))
#     days = days_in_month(year,month)
#     print(f"Количество дней в месяце: {days}")
#
# main()

#########################################################################

def ticket_price(age, show_time):
    if age < 3 :
        return 0
    elif 3<= age <=12:
        price = 10
    else:
        price = 15
    if show_time <= 12:
        price*=0.8

    return price

def main():
    age = int(input("Ввудите возраст посетителя: "))
    show_time = float(input("Введите время сеанса (например 11.35): "))
    price = ticket_price(age, show_time)
    print(f"Стоимость билета: {price:.2f}")

main()
