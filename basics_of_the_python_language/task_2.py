class DivisionByZeroError(Exception):
    def __init__(self, message="Division by zero is not allowed."):
        self.message = message
        super().__init__(self.message)


def safe_divide(a, b):
    if b == 0:
        raise DivisionByZeroError()
    return a / b


# Пример использования
try:
    num1 = int(input("Введите число: "))
    num2 = int(input("Введите делитель: "))

    result = safe_divide(num1, num2)
    print(f"Результат деления: {result}")

except ValueError:
    print("Ошибка ввода. Введите целое число.")
except DivisionByZeroError as e:
    print(f"Ошибка: {e}")
