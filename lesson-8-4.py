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
    warehouse = {'warehouse_printers': [], 'warehouse_scanners': [], 'warehouse_laptops': []}
    accountants = {'printer': [], 'scanner': [], 'laptop': []}
    programmers = {'printer': [], 'scanner': [], 'laptop': []}

    @staticmethod
    def get_warehouse():
        print("Содержимое склада: ")
        for key, value in Warehouse.warehouse.items():
            print('\033[91m', key, ':', '\033[0m')
            print(value, '\n')


class OfficeEquip:
    id = 0

    def __init__(self, model):
        self.model = model
        OfficeEquip.id += 1

    # @abstractmethod
    def make_acceptance(self):
        pass


class Printer(OfficeEquip):
    def __init__(self, model, mfu=False):
        super().__init__(model)
        self.mfu = mfu

    def __str__(self):
        return f'{self.id} {self.model} {self.mfu}'

    def make_acceptance(self):
        Warehouse.warehouse['warehouse_printers'].append([self.id, self.model, self.mfu])

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
    print('1 - вывод информации\n2 - ввод оборудования на склад\nquit - для выхода\n')
    user_key = input("Введите номер операции: ").lower()
    if user_key == 'quit':
        break
    elif user_key == '1':
        Warehouse.get_warehouse()
        # for key, value in Warehouse.warehouse.items():
        #     print('\033[91m', key, ':', '\033[0m')
        #     print(value, '\n')
    elif user_key == '2':
        user_key = input('1 - ввод принтера\n2 - ввод сканера\n3 - ввод ноутбука\nquit - выход\nВведите номер '
                         'операции: ')
        if user_key == 'quit':
            print()
            continue
        elif user_key == '1':
            name = input('Введите модель принтера: ')
            if_mfu = input('Наличие функции МФУ: (+ / - (по умолчанию)): ')
            printer_1 = Printer(name, True if if_mfu == '+' else False)
            printer_1.make_acceptance()
            Warehouse.get_warehouse()
