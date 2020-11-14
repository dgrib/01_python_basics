"""1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""
a = [1, 4, '1234', [1, 'line'], (2, 56), {'one': 'один', 'two': 'два'}, {1, '+', '&', 90}]
for i in a:
    print(type(i))

"""2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
a = list(input('Введите элементы списка: '))
j = 0
print(a)
for i in range(len(a)//2):
    a[j], a[j + 1] = a[j + 1], a[j]
    j += 2
print(a)

"""3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
"""Решение списком"""
month_number = input('Введите месяц в виде целого числа от 1 до 12: ')
compare_list = [['зима', 12, 1, 2], ['весна', 3, 4, 5], ['лето', 6, 7, 8], ['осень', 9, 10, 11]]

while not month_number.isdigit() or not 0 < int(month_number) < 13:
    month_number = input("Это не число, или оно не в диапазоне 1-12, попробуйте еще раз: ")

for i in compare_list:
    if int(month_number) in i:
        print(f'Месяц {month_number} относится к времени года: {i[0]}')
"""Решение словарем"""
# month_number = input('Введите месяц в виде целого числа от 1 до 12: ')
# compare_dict = {'зима': (12, 1, 2), 'весна': (3, 4, 5), 'лето': (6, 7, 8), 'осень': (9, 10, 11)}
# while not month_number.isdigit() or not 0 < int(month_number) < 13:
#     month_number = input("Это не число, или оно не в диапазоне 1-12, попробуйте еще раз: ")
#
# for i in compare_dict.items():
#     if int(month_number) in i[1]:
#         print(f'Месяц {month_number} относится к времени года: {i[0]}')

"""4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""
user_list = input('Введите предложение: ').split()
counter = 0
for i in user_list:
    counter += 1
    print(f'{counter} {i[:10]}')

# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.

my_list = [7, 5, 3, 3, 2]
print(my_list)
new_rate = input('Введите новый элемент рейтинга (1-9): ')
while not new_rate.isdigit() or not 0 < int(new_rate) < 10:
    new_rate = input("Это не число, или оно не в диапазоне 1-9, попробуйте еще раз: ")
new_rate = int(new_rate)

if new_rate <= my_list[-1]:
    my_list.append(new_rate)
else:
    for i in range(len(my_list)):
        if my_list[i] < new_rate:
            my_list.insert(i, new_rate)
            break
print(my_list)

# 6. * Реализовать структуру данных «Товары».
"""item_list = [
    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
    (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
]"""
check = input('Нажмите Enter чтобы ввести данные нового товара (q или й для выхода): ')
item_list = []
while check != 'й' and check != 'q':
    item_dict = dict()
    item = input('Введите наименование товара: ')
    item_dict.update({'Наименование': item})
    price = input('Введите цену товара: ')
    item_dict.update({'Цена': price})
    quantity = input('Введите количество товара: ')
    item_dict.update({'Количество': quantity})
    units = input('Введите единицу измерения товара: ')
    item_dict.update({'Ед.': units})
    check = input('Нажмите Enter чтобы ввести данные нового товара (q или й для выхода): ')
    item_list.append((len(item_list)+1, item_dict))
print('\nТовары: ')
for i in item_list:
    print(i)

analytics_dict = dict()
if len(item_list) == 0:
    print('Список товаров пуст!')
else:
    for i in item_list[0][1]:  # проходим по первому товару, создаем ключи для словаря аналитики
        analytics_set = set()
        for j in range(len(item_list)):  # проходим по списку товаров
            analytics_set.add(item_list[j][1].get(i))
        analytics_dict.update({i: list(analytics_set)})  # создаем элемент словаря аналитики

    print('\nСбор аналитики о товарах: ')
    for key, value in analytics_dict.items():
        print(key, value)
