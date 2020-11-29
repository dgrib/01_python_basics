"""5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}.')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}.')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}.')


pen_1 = Pen('Ручка_1')
pen_2 = Pen('Ручка_2')
pen_1.draw()
pen_2.draw()
pencil_3 = Pencil('Карандаш_4')
pencil_3.draw()
pencil_4 = Pencil('Карандаш_4')
pencil_4.draw()
handle_5 = Handle('Ручка_5')
handle_5.draw()
handle_6 = Handle('Ручка_6')
handle_6.draw()
