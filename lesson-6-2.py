"""2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self):
        print(f'Asphalt mass for area (length: {self._length}, width: {self._width}) = ', end='')
        print(f'{round(self._length * self._width * 25 * 5 / 1000)} t')


road_1 = Road(2500, 6)
print(road_1._length)
road_1.asphalt_mass()
road_2 = Road(5000, 8)
road_2.asphalt_mass()
