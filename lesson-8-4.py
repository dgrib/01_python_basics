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
            print('\033[37m', key, '\033[0m', sep='')
            for device in value:
                print(f'\033[1;32m{device[0]}\033[0m {" ".join(device[1:])} \033[91m *  \033[0m', end='')
            print()

    @staticmethod
    def get_offices():
        """Печатает список устройств в офисах."""
        print('\033[91m', "Устройства в офисах: ", '\033[0m', sep='')
        office_index = 0
        for office in Warehouse.offices:
            print("\033[1;34m", Warehouse.offices_names[office_index], '\033[0m', sep='')
            for key, value in office.items():
                print('\033[37m', key, '\033[0m', sep='')
                for device in value:
                    print(f'\033[1;32m{device[0]}\033[0m {" ".join(device[1:])} \033[91m *  \033[0m', end='')
                print()
            office_index += 1
        print()

    @staticmethod
    def del_device(user_id, place):
        """Takes device ID, deletes item with ID, returns: item (), item type (printer, scanner ...) """
        # warehouse = {'printers': [], 'scanners': [], 'laptops': []}
        for key, value in place.items():
            for device in value:
                if device[0] == int(user_id):
                    device_type = key  # printers, scanners ...
                    device = value.pop(value.index(device))  # устройство
                    print('\n\033[91m', f'Устройство {device} списано.', '\033[0m', sep='')
                    return device, device_type
        else:
            return 0, 0


class OfficeEquip(ABC):
    id = 0

    def __init__(self, model):
        self.model = model
        OfficeEquip.id += 1

    @abstractmethod
    def make_acceptance(self):
        pass


class Printer(OfficeEquip):
    def __init__(self, model, mfu='notMFU'):
        super().__init__(model)
        self.mfu = mfu

    def make_acceptance(self):
        """Принимает принтер на склад."""
        Warehouse.warehouse['printers'].append([self.id, self.model, self.mfu])


class Scanner(OfficeEquip):
    def __init__(self, model, size='A4'):
        super().__init__(model)
        self.size = size

    def make_acceptance(self):
        """Принимает сканер на склад."""
        Warehouse.warehouse['scanners'].append([self.id, self.model, self.size])


class Laptop(OfficeEquip):
    def __init__(self, model, software):
        super().__init__(model)
        self.software = software

    def make_acceptance(self):
        """Принимает ноутбук на склад."""
        Warehouse.warehouse['laptops'].append([self.id, self.model, self.software])


Printer('Canon 6600').make_acceptance()
Printer('Canon 250').make_acceptance()
Scanner('Canon LiDE 300').make_acceptance()
Scanner('BROTHER ADS-2200').make_acceptance()
Scanner('Epson WorkForce DS-1630').make_acceptance()
Warehouse.offices[0]['scanners'].append(Warehouse.del_device(5, Warehouse.warehouse)[0])
Laptop('APPLE MacBook Air 13.3"', 'Windows, Office, 1c').make_acceptance()
Laptop('LENOVO IdeaPad 5', 'Linux').make_acceptance()
Warehouse.offices[1]['laptops'].append(Warehouse.del_device(7, Warehouse.warehouse)[0])
Printer('KYOCERA Ecosys M2735dn', 'MFU').make_acceptance()
Warehouse.offices[1]['printers'].append(Warehouse.del_device(8, Warehouse.warehouse)[0])
Printer('EPSON L132', 'notMFU').make_acceptance()
Warehouse.offices[0]['printers'].append(Warehouse.del_device(9, Warehouse.warehouse)[0])

clear()
while True:
    print()
    print('1 - Вывод информации (устройства на складе и в офисах)\n2 - Занести устройство на склад\n'
          '3 - Перенести устройство со склада в отдел\n4 - Удаление устройств (со склада и из офисов)\n')
    user_key = input("Введите номер операции (quit - Выход): ").lower()
    # Главное меню.
    if user_key == 'quit':
        break
    # Вывод информации
    elif user_key == '1':
        Warehouse.get_warehouse()
        print()
        Warehouse.get_offices()
    # Занести устройство на склад
    elif user_key == '2':
        while True:
            user_key = input('1 - принтер\n2 - сканер\n3 - ноутбук\nКакое устройство вы '
                             'хотите занести на склад? (quit - выход): ')
            # Меню ввода устройства на склад.
            if user_key == 'quit':
                print()
                break
            elif user_key == '1':
                name = input('Введите модель принтера (например Cannon 6500): ')
                if_mfu = '0'
                # проверка ввода + или - для характеристики принтера МФУ.
                while if_mfu not in '+-':
                    if_mfu = input('Введите наличие функции МФУ (+ / -): ')
                printer_1 = Printer(name, 'MFU' if if_mfu == '+' else 'notMFU')
                printer_1.make_acceptance()
                Warehouse.get_warehouse()
            elif user_key == '2':
                name = input('Введите модель сканера (например Cannon 6500): ')
                scan_format = ''
                # проверка ввода формата типа А3, А4 ...
                while len(scan_format) != 2 or (scan_format[0] not in 'AaАа' or not scan_format[1].isdigit()):
                    scan_format = input('Формат сканера (например А4, A3 ...): ').upper()
                scan_1 = Scanner(name, scan_format)
                scan_1.make_acceptance()
                Warehouse.get_warehouse()
            elif user_key == '3':
                name = input('Введите модель ноутбука (например APPLE MacBook Air 13.3"): ')
                laptop_soft = input('Введите soft ноутбука (например Windows, Office): ')
                laptop_1 = Laptop(name, laptop_soft)
                laptop_1.make_acceptance()
                Warehouse.get_warehouse()
    # Перенести устройство со склада в отдел
    elif user_key == '3':
        Warehouse.get_warehouse()
        # ввод ID устройства на складе для переноса в отдел
        while True:
            user_id = input('Выберите ID устройства (зеленая цифра) для переноса в отдел (quit для выхода): ')
            if user_id == 'quit':
                print()
                break
            elif user_id.isdigit():
                # проверка, есть ли введенное ID на складе
                id_list = []
                list([id_list.append(j[0]) for j in i] for i in Warehouse.warehouse.values())
                if int(user_id) in id_list:
                    break
        # ввод отдела для переноса в него устройства
        while True:
            user_office = input('1 - Бухгалтерия\n2 - Программисты\n'
                                'Введите отдел для переноса устройства (quit - выход): ')
            if user_office == 'quit':
                print()
                break
            elif user_office.isdigit() and int(user_office) - 1 in range(len(Warehouse.offices)):
                # Удаляем устройство со склада и возвращаем устройство и его тип (принтер, сканер ...)
                device, device_type = Warehouse.del_device(user_id, Warehouse.warehouse)
                # добавляем устройство device типа device_type в отдел user_office.
                Warehouse.offices[int(user_office) - 1][device_type].append(device)
                print(f'Устройство {device[1]} добавлено в отдел: {Warehouse.offices_names[int(user_office) - 1][:-2]}.')
                break
    # Удаление устройств
    elif user_key == '4':
        Warehouse.get_warehouse()
        Warehouse.get_offices()
        while True:
            user_id = input('Выберите ID устройства (зеленая цифра) для удаления (quit для выхода): ')
            if user_id == 'quit':
                print()
                break
            elif user_id.isdigit():
                Warehouse.del_device(int(user_id), Warehouse.warehouse)
                Warehouse.del_device(int(user_id), Warehouse.accountants)
                Warehouse.del_device(int(user_id), Warehouse.programmers)
