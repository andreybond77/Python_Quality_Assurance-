# utils/logger.py
import logging
from functools import wraps
import time

# --- Настройка логирования ---
# Или создадим логгер для декоратора
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Создаем обработчик для вывода в консоль
console_handler = logging.StreamHandler()
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)

# Добавляем обработчик к логгеру, если он еще не добавлен
if not logger.handlers:
    logger.addHandler(console_handler)

def log_calls(func):
    """
    Декоратор для логирования вызовов функций, их аргументов, возвращаемого значения и времени выполнения.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Формируем строку с аргументами для лога
        # args[0] обычно 'self', пропускаем его для методов
        args_str = ', '.join([repr(arg) for arg in args[1:]]) # Пропускаем первый аргумент (self)
        kwargs_str = ', '.join([f"{k}={repr(v)}" for k, v in kwargs.items()])
        all_args_str = ', '.join(filter(None, [args_str, kwargs_str]))

        # Логируем начало вызова
        logger.info(f"Вызов метода '{func.__name__}' с аргументами: ({all_args_str})")

        start_time = time.time()

        try:
            # Выполняем оригинальный метод
            result = func(*args, **kwargs)
            execution_time = time.time() - start_time

            # Логируем успешный результат
            logger.info(f"Метод '{func.__name__}' завершен успешно. "
                        f"Результат: {repr(result)}. "
                        f"Время выполнения: {execution_time:.4f} секунд.")
            return result

        except Exception as e:
            execution_time = time.time() - start_time
            # Логируем ошибку
            logger.error(f"Метод '{func.__name__}' вызвал исключение: {type(e).__name__}: {e}. "
                         f"Время выполнения до ошибки: {execution_time:.4f} секунд.")
            # Пробрасываем исключение дальше
            raise

    return wrapper



