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
from abc import ABC
from abc import abstractmethod


class Closing(ABC):
    sum_square = 0
    sum_name = []

    def __init__(self, name, size):
        self.size = size
        self.name = name
        self.get_square

    @abstractmethod
    def get_square(self):
        pass

    @staticmethod
    def get_total_square():
        return f'Total material square: {" + ".join(Closing.sum_name)} = {Closing.sum_square:.3f} m2'


class Coat(Closing):
    sum_square = None
    sum_name = None

    @property
    def get_square(self):
        square = self.size / 6.5 + 0.5
        Closing.sum_square += square
        Closing.sum_name.append(self.name)
        print(f'Square of {self.name}: {square :.3f} m2')
        return None


class Suit(Closing):
    sum_square = None
    sum_name = None

    @property
    def get_square(self):
        square = 2 * self.size + 0.3
        Closing.sum_square += square
        Closing.sum_name.append(self.name)
        print(f'Square of {self.name}: {square :.3f} m2')
        return None


# coat sizes: 40...58
# height sizes for suit: 1.00...2.40 m
coat_1 = Coat("coat_1", 40)
# print(coat_1.get_square)
coat_2 = Coat("coat_2", 52)
# print(coat_2.get_square)
suit_1 = Suit("suit_1", 1.20)
# print(suit_1.get_square)
suit_2 = Suit("suit_2", 2.05)
# print(suit_2.get_square)
print(Closing.get_total_square())
