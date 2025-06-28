# def fibonacci(n):
#     if n < 0:
#         raise ValueError("Число n должно быть положительным")
#     elif n == 0:
#       return 0
#     elif n ==1:
#         return  1
#     else: return  fibonacci(n-1)+fibonacci(n-2)
#
# def main():
#     print("=== Вычисление чисел Фибоначчи ===")
#     try:
#         n = int(input("Введите положительное число n: "))
#         if n <0:
#             print("Ошибка: число должно быть положительным.")
#         else:
#             result= fibonacci(n)
#             print(f"Число Фибоначчи с индексом {n}: {result}")
#     except ValueError as e:
#         print(f"Ошибка: {e}")
#
# if __name__=="__main__" :
#     main()

def F(n):
    if n>2:
        return  F(n-1)+G(n-2)
    else: return n
def G(n):
    if n>2:
        return  G(n-1)+ F(n-2)
    else: return n+1
    
if __name__ == "__main__":
    print("F(4):", F(4))  # Ожидаемый результат: 7
    print("G(4):", G(4))  # Ожидаемый результат: 6
    print("F(5):", F(5))  # Дополнительный тест
    print("G(5):", G(5))  # Дополнительный тест