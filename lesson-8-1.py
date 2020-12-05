"""1. Реализовать класс «Дата»,
функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def take_date(cls, date):
        try:
            day, month, year = tuple(map(int, date.split('-')))
            return cls(day, month, year)
        except ValueError:
            print(f"{date} Введите дату в численном формате!")
            # вызываем ошибку валидации
            return cls(0, 0, 0)

    @staticmethod
    def validation(obj):
        if 0 < obj.day <= 31 and 0 < obj.month <= 12 and 0 < obj.year <= 9999:
            return f'{obj.day} {obj.month} {obj.year} корректраня дата!'
        else:
            return f'Некорректная дата!'


date_1 = Date.take_date('24-12-2020')
print(Date.validation(date_1))
print()
date_2 = Date.take_date('19-13-2020')
print(Date.validation(date_2))
print()
date_3 = Date.take_date('ab-12-2020')
print(Date.validation(date_3))
