"""7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
начиная с 1! и до n!."""


def fact(elem):
    """Gives factorial generator."""
    fac = 1
    for j in range(elem + 1):
        if j == 0:
            yield 1
        else:
            fac *= j
            yield fac


n = int(input("Enter a number for factorial: "))
print(fact(n))  # proves we have generator object

num = 0
for el in fact(n):
    print(f"{num}! = {el}")
    num += 1
