"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
"""


class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


num = int(input("Введите делимое число: "))
divider = int(input("Введите делитель, не равный 0: "))
while True:
    try:
        if divider == 0:
            raise ZeroError("Вы ввели 0, попробуйте еще раз!")
        else:
            print(f'{num / divider:.5f}')
            break
    except ZeroError as err:
        print(err)
        divider = int(input("Введите делитель, не равный 0: "))
