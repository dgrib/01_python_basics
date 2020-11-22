"""1 Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""
# надо вводить скрипт типа: python lesson-4-1.py 160 50 600

from sys import argv

if len(argv) == 4:
    work_hours, salary_pro_hour, bonus = argv[1:]
    try:
        if float(work_hours) > 0 and float(salary_pro_hour) and float(bonus) > 0:
            salary = float(work_hours) * float(salary_pro_hour) + float(bonus)
            print(f"Employee's salary is: {salary:.2f} dollars")
        else:
            print('Some data is not positive. Enter 3 positive params.')
    except ValueError:
        print('Your data are not numbers.')
else:
    print('Not enough data. Enter 3 positive params.')

"""2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента."""
# my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
#
# print([my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]])

"""3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку."""
# print([i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0])

"""4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор."""
# my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
#
# print([i for i in my_list if my_list.count(i) == 1])

"""5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка."""
# from functools import reduce
#
# print(reduce(lambda arg_1, arg_2: arg_1 * arg_2, [i for i in range(100, 1001) if i % 2 == 0]))

"""6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools."""
# надо вводить скрипт типа: python lesson-4-6.py 3 my_string

# from sys import argv
# from itertools import count
# from itertools import cycle
#
# num_count, num_cycle = argv[1:]
#
# for el in count(int(num_count)):
#     if el > 10:
#         break
#     else:
#         print(el)
#
# c = 1
# for el in cycle(num_cycle):
#     if c > 10:
#         break
#     print(el)
#     c += 1

"""7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
начиная с 1! и до n!."""


# def fact(elem):
#     """Gives factorial generator."""
#     fac = 1
#     for j in range(elem + 1):
#         if j == 0:
#             yield 1
#         else:
#             fac *= j
#             yield fac
#
#
# n = int(input("Enter a number for factorial: "))
# print(fact(n))  # proves we have generator object
#
# num = 0
# for el in fact(n):
#     print(f"{num}! = {el}")
#     num += 1
