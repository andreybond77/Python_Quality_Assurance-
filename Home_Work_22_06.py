#
#
#
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side,side)
#
#     @property
#     def side(self):
#         return self.width
#
#     @side.setter
#     def side (self, value):
#         self.width = value
#         self.height = value
#
# if __name__ == "__main__":
#     # Создание прямоугольника
#     rectangle = Rectangle(4, 5)
#     print("Прямоугольник:")
#     print(f"Площадь: {rectangle.area()}")
#     print(f"Периметр: {rectangle.perimeter()}")
#
#     # Создание квадрата
#     square = Square(4)
#     print("\nКвадрат:")
#     print(f"Площадь: {square.area()}")
#     print(f"Периметр: {square.perimeter()}")
#
#     # Изменение стороны квадрата
#     square.side = 6
#     print("\nИзмененный квадрат:")
#     print(f"Площадь: {square.area()}")
#     print(f"Периметр: {square.perimeter()}")

##################################################################

# Класс Person
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):

        print(f"Привет! Меня зовут {self.name}. Мне {self.age} лет, и я {self.gender}.")


# Класс Employee, наследующий Person
class Employee(Person):
    def __init__(self, name, age, gender, salary, position):

        super().__init__(name, age, gender)  # Вызываем конструктор родительского класса
        self.salary = salary
        self.position = position

    def work(self):

        print(f"Я работаю как {self.position} и получаю зарплату {self.salary} рублей.")


# Пример использования
if __name__ == "__main__":
    # Создание объекта Person
    person = Person("Анна", 30, "женщина")
    print("Информация о человеке:")
    person.introduce()

    # Создание объекта Employee
    employee = Employee("Иван", 25, "мужчина", 50000, "разработчик")
    print("\nИнформация о сотруднике:")
    employee.introduce()  # Метод из класса Person
    employee.work()       # Метод из класса Employee