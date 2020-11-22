"""6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools."""
# надо вводить скрипт типа: python lesson-4-6.py 3 my_string
from sys import argv
from itertools import count
from itertools import cycle

num_count, num_cycle = argv[1:]

for el in count(int(num_count)):
    if el > 10:
        break
    else:
        print(el)

c = 1
for el in cycle(num_cycle):
    if c > 10:
        break
    print(el)
    c += 1
