"""1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой
матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""
from itertools import zip_longest


class Matrix:
    """Matrices sum count."""

    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        m_sum = []
        for sublist in zip_longest(self.matrix, other.matrix, fillvalue=[]):
            temp = []
            for numbers in zip_longest(sublist[0], sublist[1], fillvalue=0):
                temp.append(sum(numbers))
            m_sum.append(temp)
        return Matrix(m_sum)

    def __str__(self):
        answer = ''
        for i in self.matrix:
            answer += " ".join([f'{x:3}' for x in i]) + '\n'
        return answer


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_3 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_4 = Matrix([[1, 2, 3, 3], [4, 5, 6, 6], [7, 8, 9, 9]])
matrix_5 = Matrix([[1, 2, 3], [4, 5, 6]])
print(matrix_1 + matrix_2 + matrix_3)
print(matrix_1 + matrix_4 + matrix_5)


"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
# from abc import ABC
# from abc import abstractmethod
#
#
# def get_total_square():
#     return f'Total material square: {" + ".join(Closing.sum_name)} = {Closing.sum_square:.3f} m2'
#
#
# class Closing(ABC):
#     sum_square = 0
#     sum_name = []
#
#     @abstractmethod
#     def get_square(self):
#         pass
#
#
# class Coat(Closing):
#     def __init__(self, name, size):
#         self.size = size
#         self.name = name
#
#     @property
#     def get_square(self):
#         square = self.size / 6.5 + 0.5
#         Closing.sum_square += square
#         Closing.sum_name.append(self.name)
#         return f'Square of {self.name}: {square :.3f} m2'
#
#
# class Suit(Closing):
#     def __init__(self, name, size):
#         self.size = size
#         self.name = name
#
#     @property
#     def get_square(self):
#         square = 2 * self.size + 0.3
#         Closing.sum_square += square
#         Closing.sum_name.append(self.name)
#         return f'Square of {self.name}: {square :.3f} m2'
#
#
# # coat sizes: 40...58
# # height sizes for suit: 1.00...2.40 m
# coat_1 = Coat("coat_1", 40)
# print(coat_1.get_square)
# coat_2 = Coat("coat_2", 52)
# print(coat_2.get_square)
# suit_1 = Suit("suit_1", 1.20)
# print(suit_1.get_square)
# suit_2 = Suit("suit_2", 2.05)
# print(suit_2.get_square)
# print(get_total_square())


"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только
если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух.
Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""


# class Cell:
#     def __init__(self, cells):
#         self.cells = int(cells)
#
#     def __add__(self, other):
#         return Cell(self.cells + other.cells)
#
#     def __sub__(self, other):
#         return Cell(self.cells - other.cells) if self.cells > other.cells else "Subtraction is less than 0"
#
#     def __mul__(self, other):
#         return Cell(self.cells * other.cells)
#
#     def __truediv__(self, other):
#         return Cell(round(self.cells / other.cells))
#
#     def make_order(self, num):
#         """Returns num pieces in a row like *****\n*****\n***"""
#         return (('*' * num) + '\n') * (self.cells // num) + str(self.cells % num * '*')
#
#     def __str__(self):
#         return f'Cells quantity: {str(self.cells)}'
#
#
# cell_1 = Cell(12)
# cell_2 = Cell(10)
# cell_3 = Cell(2)
# print(cell_1 + cell_2 + cell_3)
# print(cell_1 - cell_2)
# print(cell_3 - cell_1)
# print(cell_1 * cell_2)
# print(cell_1 / cell_2)
# print(cell_1.make_order(5))
# print(Cell(15) + Cell(12) + Cell(5))
# print((Cell(15) + Cell(12) + Cell(5)).make_order(10))
