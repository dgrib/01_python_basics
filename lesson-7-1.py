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
    def __init__(self, m):
        self.m = m

    def __add__(self, other):
        # m_sum = []
        # for sublist in zip_longest(self.m, other.m, fillvalue=[]):
        #     print(sublist)
        #     temp = []
        #     for numbers in zip_longest(sublist[0], sublist[1], fillvalue=0):
        #         temp.append(sum(numbers))
        #     m_sum.append(temp)
        # return Matrix(m_sum)
        return Matrix([(sum(_)) for _ in zip_longest(*t, fillvalue=0)]
                      for t in zip_longest(self.m, other.m, fillvalue=[]))

    def __str__(self):
        # answer = ''
        # for i in self.matrix:
        #     answer += " ".join([f'{x:3}' for x in i]) + '\n'
        # return answer
        return '\n'.join(' '.join([f'{x:3}' for x in i]) for i in self.m) + '\n'


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_3 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_4 = Matrix([[1, 2, 3, 3], [4, 5, 6, 6], [7, 8, 9, 9]])
matrix_5 = Matrix([[1, 2, 3], [4, 5, 6]])
print(matrix_1 + matrix_2 + matrix_3)
print(matrix_1 + matrix_4 + matrix_5)
