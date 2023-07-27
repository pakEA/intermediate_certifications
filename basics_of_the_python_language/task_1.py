class Date:
    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def extract_values(cls, date_str):
        day, month, year = map(int, date_str.split('-'))
        return day, month, year

    @staticmethod
    def validate_date(day, month, year):
        if not (1 <= day <= 31):
            raise ValueError("Invalid day. Day should be between 1 and 31.")
        if not (1 <= month <= 12):
            raise ValueError("Invalid month. Month should be between 1 and 12.")
        if not (year >= 0):
            raise ValueError("Invalid year. Year should be a positive number.")

    def get_date(self):
        day, month, year = self.extract_values(self.date_str)
        self.validate_date(day, month, year)
        return f"{day:02d}-{month:02d}-{year:04d}"


# Пример использования
try:
    date_str = "27-07-2023"
    date = Date(date_str)
    print(date.get_date())  # Вывод: 27-07-2023

    invalid_date_str = "32-13-2023"
    invalid_date = Date(invalid_date_str)
    print(invalid_date.get_date())  # Вывод: ValueError: Invalid day. Day should be between 1 and 31.

except ValueError as e:
    print(f"Error: {e}")
