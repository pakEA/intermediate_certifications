class Warehouse:
    def __init__(self):
        self.equipment_inventory = {}

    def add_equipment(self, equipment, quantity=1):
        if equipment in self.equipment_inventory:
            self.equipment_inventory[equipment] += quantity
        else:
            self.equipment_inventory[equipment] = quantity

    def transfer_equipment(self, equipment, quantity, department):
        if equipment in self.equipment_inventory and self.equipment_inventory[equipment] >= quantity:
            self.equipment_inventory[equipment] -= quantity
            print(f"{quantity} единиц оргтехники {equipment} переданы в подразделение {department}.")
        else:
            print(f"Недостаточно оргтехники {equipment} на складе.")

    def show_inventory(self):
        print("Список оргтехники на складе:")
        for equipment, quantity in self.equipment_inventory.items():
            print(f"{equipment} - {quantity} шт.")

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

    warehouse.add_equipment(printer1, 5)
    warehouse.add_equipment(scanner1, 3)
    warehouse.add_equipment(xerox1, 2)

    warehouse.show_inventory()

    warehouse.transfer_equipment(printer1, 2, "Отдел продаж")
    warehouse.transfer_equipment(scanner1, 4, "Отдел маркетинга")
    warehouse.transfer_equipment(xerox1, 1, "Бухгалтерия")

    warehouse.show_inventory()
