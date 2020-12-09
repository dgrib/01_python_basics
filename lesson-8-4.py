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


class Warehouse:
    warehouse = {'printers': [], 'scanners': [], 'laptops': []}
    accountants = {'printers': [], 'scanners': [], 'laptops': []}
    programmers = {'printers': [], 'scanners': [], 'laptops': []}
    offices = [accountants, programmers]

    @staticmethod
    def get_warehouse():
        print("Содержимое склада: ")
        for key, value in Warehouse.warehouse.items():
            print('\033[91m', key, ':', '\033[0m')
            print(value)

    @staticmethod
    def del_device():
        while True:
            user_id = input('Выберите ID устройства для удаления (quit для выхода): ')
            if user_id == 'quit':
                print()
                break
            elif user_id.isdigit():
                for key, value in Warehouse.warehouse.items():
                    for device in value:
                        if device[0] == int(user_id):
                            device_type = key  # index устройства
                            device = el.pop(0)  # устройство
                            print('\n\033[91m', f'Устройство {device} удалено', '\033[0m', sep='')
                # break
        return device, device_type


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

    def __str__(self):
        return f'{self.id} {self.model} {self.mfu}'

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
printer_2 = Printer('Canon 250')
print(printer_1)
printer_1.make_acceptance()

print(Warehouse.warehouse)

while True:
    print('1 - Вывод информации\n2 - Занести устройство на склад\n'
          '3 - Перенести устройство со склада в отдел\n4 - Удалить устройство\nquit - Выход\n')
    user_key = input("Введите номер операции: ").lower()
    if user_key == 'quit':
        break
    elif user_key == '1':
        Warehouse.get_warehouse()
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
        device, device_type = Warehouse.del_device()
        # [2, wsf? wef]

        print('1 - Бухгалтерия>\n2 - Программисты\nquit - выход\nВведите номер отдела: ')
        user_office = input('Введите отдел для переноса устройства: ')
        if user_office == 'quit':
            print()
            continue
        elif user_office.isdigit():
            Warehouse.offices[int(user_office) - 1][device_type].append(device)
            # for office in range(1, len(Warehouse.offices)):
            print(Warehouse.offices)

            # accountants = {'printers': [], 'scanners': [], 'laptops': []}
            # programmers = {'printers': [], 'scanners': [], 'laptops': []}
            # offices = [accountants, programmers]
            # for el in Warehouse.warehouse.values():
            #     for device in el:
            #         if device[0] == int(user_office):
            #             device = el.pop(0)
            #             print('\n\033[91m', f'Устройство {device} удалено', '\033[0m', sep='')
    elif user_key == '4':
        Warehouse.get_warehouse()
        Warehouse.del_device()
