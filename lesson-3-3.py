"""3 Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(first, second, third):
    """Prints 2 max arguments sum of 3"""
    try:
        first = float(first)
        second = float(second)
        third = float(third)
        my_list = [first, second, third]
        # my_list.remove(min(my_list)) нерационально снова пробегать список чтобы удалить
        return f'2 max arguments sum of {first}, {second}, {third} = {sum(my_list) - min(my_list):.2f}'
    except ValueError as v:
        return 'Enter numbers. Try again.'


print(my_func(input('Enter first argument: '), input('Enter second argument: '), input('Enter third argument: ')))
