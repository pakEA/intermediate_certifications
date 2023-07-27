class Warehouse:
    def __init__(self):
        self.equipment_list = []

    def add_equipment(self, equipment):
        self.equipment_list.append(equipment)

    def show_inventory(self):
        print("Список оргтехники на складе:")
        for equipment in self.equipment_list:
            print(equipment)


class OfficeEquipment:
    def __init__(self, brand, model, serial_number):
        self.brand = brand
        self.model = model
        self.serial_number = serial_number

    def __str__(self):
        return f"{self.brand} {self.model} (SN: {self.serial_number})"


class Printer(OfficeEquipment):
    def __init__(self, brand, model, serial_number, printer_type):
        super().__init__(brand, model, serial_number)
        self.printer_type = printer_type

    def __str__(self):
        return f"Принтер: {super().__str__()}, Тип: {self.printer_type}"


class Scanner(OfficeEquipment):
    def __init__(self, brand, model, serial_number, scanner_resolution):
        super().__init__(brand, model, serial_number)
        self.scanner_resolution = scanner_resolution

    def __str__(self):
        return f"Сканер: {super().__str__()}, Разрешение: {self.scanner_resolution}"


class Xerox(OfficeEquipment):
    def __init__(self, brand, model, serial_number, copy_speed):
        super().__init__(brand, model, serial_number)
        self.copy_speed = copy_speed

    def __str__(self):
        return f"Ксерокс: {super().__str__()}, Скорость копирования: {self.copy_speed} стр/мин"


# Пример использования
if __name__ == "__main__":
    warehouse = Warehouse()

    printer1 = Printer("HP", "LaserJet Pro M402n", "123456789", "лазерный")
    scanner1 = Scanner("Epson", "Perfection V600", "987654321", "4800 dpi")
    xerox1 = Xerox("Canon", "i-SENSYS MF3010", "456789123", "18")

    warehouse.add_equipment(printer1)
    warehouse.add_equipment(scanner1)
    warehouse.add_equipment(xerox1)

    warehouse.show_inventory()
