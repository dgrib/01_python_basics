"""1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой
матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    """Matrices sum count."""
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        # дописать проверку для разноранговых матриц
        # или заменять нулями несуществующие элементы
        m_sum = []
        for sublist in zip(self.matrix, other.matrix):
            temp = []
            for numbers in zip(sublist[0], sublist[1]):
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
print(matrix_1 + matrix_2 + matrix_3)

