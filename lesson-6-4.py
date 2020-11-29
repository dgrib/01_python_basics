"""4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
from random import choice


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Auto {self.name} started to go.')

    def stop(self):
        print(f'Auto {self.name} stopped.')

    def turn(self):
        print(f'Auto {self.name} turned {choice(["Left", "Right"])}.')

    def show_speed(self):
        print(f'Speed of {self.name} = {self.speed} km/h.')

    def police(self):
        if self.is_police:
            print(f'{self.name} is a police car.')
        else:
            print(f'{self.name} is NOT a police car.')


class TownCar(Car):
    def show_speed(self):
        print(f'Speed of {self.name} = {self.speed} km/h.')
        if self.speed > 60:
            print('Excessive speed !!!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Speed of {self.name} = {self.speed} km/h.')
        if self.speed > 40:
            print('Excessive speed !!!')


class PoliceCar(Car):
    pass


town_car = TownCar(50, 'green', 'Toyota', False)
print(town_car.name)
town_car.police()
town_car.go()
town_car.show_speed()
town_car.speed = 65
town_car.show_speed()
town_car.stop()
print()
sport_car = SportCar(250, 'white', 'Lada', False)
print(sport_car.name, sport_car.color)
sport_car.go()
sport_car.show_speed()
sport_car.turn()
sport_car.stop()
print()
work_car = WorkCar(55, 'brown', 'Kamaz', False)
work_car.go()
work_car.show_speed()
work_car.speed = 20
work_car.show_speed()
work_car.turn()
work_car.stop()
print()
police_car = PoliceCar(30, 'yellow', 'Nissan', True)
print(police_car.name)
police_car.police()
police_car.go()
police_car.show_speed()
police_car.turn()
police_car.stop()
