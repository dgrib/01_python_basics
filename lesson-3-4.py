"""4 Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
"""


def my_func(x, y):
    """Raises x (x>0) to the power of y (y<0)"""
    if x <= 0 or y >= 0:
        return 'x must be float type and greater than 0, y must be int type and less than 0'
    else:
        num = x
        for i in range(abs(y)-1):
            num *= x
        return 1 / num


x = float(input('Enter a positive number: '))
y = int(input('Enter a negative number: '))
print(my_func(x, y))

