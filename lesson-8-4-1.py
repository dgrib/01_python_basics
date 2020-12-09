"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""
"""5. Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.
"""
"""6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""
from abc import ABC
from abc import abstractmethod


def clear():
    """Очищает экран."""
    print('\n' * 10)


class Warehouse:
    warehouse = {'printers': [], 'scanners': [], 'laptops': []}
    accountants = {'printers': [], 'scanners': [], 'laptops': []}
    programmers = {'printers': [], 'scanners': [], 'laptops': []}
    offices = [accountants, programmers]
    offices_names = ['Бухгалтерия: ', 'Программисты: ']

    @staticmethod
    def get_warehouse():
        """Печатает список устройств на складе."""
        clear()
        print('\033[91m', "Устройства на складе: ", '\033[0m', sep='')
        for key, value in Warehouse.warehouse.items():
            print(key)
            for device in value:
                print('ID =', *device, '\033[91m * \033[0m', end='')
            print()

    @staticmethod
    def get_offices():
        """Печатает список устройств в офисах."""
        print('\033[91m', "Устройства в офисах: ", '\033[0m', sep='')
        office_index = 0
        for office in Warehouse.offices:
            print(Warehouse.offices_names[office_index])
            for key, value in office.items():
                print('\033[91m', key, ':', '\033[0m')
                print(value)
            office_index += 1

    @staticmethod
    def del_device(user_id):
        """Takes device ID, deletes item with ID, returns: item (), item type (printer, scanner ...) """
        for key, value in Warehouse.warehouse.items():
            for device in value:
                if device[0] == int(user_id):
                    device_type = key  # printers
                    device = value.pop(value.index(device))  # устройство
                    print('\n\033[91m', f'Устройство {device} удалено со склада.', '\033[0m', sep='')
                    return device, device_type
                else:
                    return 0, 0


class OfficeEquip:
    id = 0

    def __init__(self, model):
        self.model = model
        OfficeEquip.id += 1

    # @abstractmethod
    def make_acceptance(self):
        pass


class Printer(OfficeEquip):
    def __init__(self, model, mfu='Not MFU'):
        super().__init__(model)
        self.mfu = mfu

    # def __str__(self):
    #     return f'{self.id} {self.model} {self.mfu}'

    def make_acceptance(self):
        Warehouse.warehouse['printers'].append([self.id, self.model, self.mfu])

    def to_some_office(self):
        pass


# class Scanner(OfficeEquip):
#     def __init__(self, model, size='A4'):
#         super().__init__(model)
#         self.size = size
#
#     def make_acceptance(self):
#         pass


# class Laptop(OfficeEquip):
#     def __init__(self, model, software):
#         super().__init__(model)
#         self.software = software
#
#     def make_acceptance(self):
#         pass


printer_1 = Printer('Canon 6600')
printer_1.make_acceptance()
printer_2 = Printer('Canon 250')
printer_2.make_acceptance()

print(Warehouse.warehouse)

while True:
    print('1 - Вывод информации\n2 - Занести устройство на склад\n'
          '3 - Перенести устройство со склада в отдел\n4 - Удаление устройств\nquit - Выход\n')
    user_key = input("Введите номер операции: ").lower()
    if user_key == 'quit':
        break
    elif user_key == '1':
        Warehouse.get_warehouse()
        Warehouse.get_offices()
    elif user_key == '2':
        user_key = input('1 - принтер\n2 - сканер\n3 - ноутбук\nquit - выход\nВведите номер '
                         'операции: ')
        if user_key == 'quit':
            print()
            continue
        elif user_key == '1':
            name = input('Введите модель принтера: ')
            if_mfu = input('Наличие функции МФУ: (+ / - (по умолчанию)): ')
            printer_1 = Printer(name, 'MFU' if if_mfu == '+' else 'Not MFU')
            printer_1.make_acceptance()
            Warehouse.get_warehouse()
    elif user_key == '3':
        Warehouse.get_warehouse()
        user_id = input('Выберите ID устройства для переноса в отдел (quit для выхода): ')
        user_office = input('1 - Бухгалтерия\n2 - Программисты\nquit - выход\nВведите отдел для переноса устройства: ')
        device, device_type = Warehouse.del_device(user_id)
        print(device, device_type)
        if user_office == 'quit':
            print()
            continue
        elif user_office.isdigit():
            # добавляем устройство с индексом user_office в отдел
            Warehouse.offices[int(user_office) - 1][device_type].append(device)
            Warehouse.get_offices()
    elif user_key == '4':
        Warehouse.get_warehouse()
        while True:
            user_id = input('Выберите ID устройства для удаления (quit для выхода): ')
            if user_id == 'quit':
                print()
                break
            elif user_id.isdigit():
                Warehouse.del_device(int(user_id))
