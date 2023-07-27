class NonNumericInputError(Exception):
    def __init__(self, input_value):
        self.input_value = input_value
        super().__init__(f"Invalid input: '{input_value}' is not a number.")


def get_numeric_input():
    while True:
        try:
            user_input = input("Введите число (или 'stop' для завершения): ")

            if user_input.lower() == 'stop':
                break

            numeric_value = float(user_input)
            if not user_input.replace('.', '').isdigit():
                raise NonNumericInputError(user_input)

            yield numeric_value

        except ValueError:
            print("Ошибка: Введите число.")
        except NonNumericInputError as e:
            print(f"Ошибка: {e}")


# Пример использования
if __name__ == "__main__":
    number_list = list(get_numeric_input())
    print("Список с числами:", number_list)
