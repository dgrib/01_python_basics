"""1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""
f_obj = open("dz_5_1.txt", "w", encoding='utf-8')
string = " "
while string:
    string = input("Enter data: ")
    print(string, file=f_obj) if string else f_obj.close()



