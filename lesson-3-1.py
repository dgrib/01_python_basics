"""1 Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division_2numbers(first, second):
    """Divides 2 numbers"""
    try:
        print(f'{first} / {second} = {first / second}')
    except ZeroDivisionError as zero_div:
        print(f'{zero_div}')


division_2numbers(float(input('Введите делимое: ')), float(input('Введите делитель: ')))
