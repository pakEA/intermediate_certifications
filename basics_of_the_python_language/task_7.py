class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            real_sum = self.real + other.real
            imag_sum = self.imag + other.imag
            return ComplexNumber(real_sum, imag_sum)
        else:
            raise ValueError("Addition is only supported for ComplexNumber objects.")

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            real_mul = self.real * other.real - self.imag * other.imag
            imag_mul = self.real * other.imag + self.imag * other.real
            return ComplexNumber(real_mul, imag_mul)
        else:
            raise ValueError("Multiplication is only supported for ComplexNumber objects.")


# Пример использования
if __name__ == "__main__":
    # Создаем два комплексных числа
    num1 = ComplexNumber(2, 3)
    num2 = ComplexNumber(4, 5)

    # Сложение комплексных чисел
    sum_result = num1 + num2
    print(f"Сумма: {sum_result}")

    # Умножение комплексных чисел
    mul_result = num1 * num2
    print(f"Произведение: {mul_result}")
