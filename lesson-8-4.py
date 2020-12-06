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
    acceptance = {'printer': [], 'scanner': [], 'laptop': []}
    project_team = {'printer': [], 'scanner': [], 'laptop': []}
    sales_team = {'printer': [], 'scanner': [], 'laptop': []}

    # def to_project_team(self):


class OfficeEquip:
    id = 0

    def __init__(self, model):
        self.model = model
        OfficeEquip.id += 1
        self.type = ''

    # @abstractmethod
    def make_acceptance(self):
        pass


class Printer(OfficeEquip):
    def __init__(self, model, mfu=False):
        super().__init__(model)
        self.mfu = mfu
        self.type = 'printer'

    def __str__(self):
        return f'{self.id} {self.model} {self.mfu}'

    def make_acceptance(self):
        Warehouse.acceptance['printer'].append([self.id, self.type, self.model, self.mfu])

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
print(printer_1)
printer_1.make_acceptance()
print(Warehouse.acceptance)
