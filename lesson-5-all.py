"""1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""
# f_obj = open("dz_5_1.txt", "w", encoding='utf-8')
# while True:
#     string = input("Enter data: ")
#     if string != "":
#         print(string, file=f_obj)
#     else:
#         break
#
# f_obj.close()


"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""
# with open('dz_5_2.txt', 'r', encoding='utf-8') as f_obj:
#     for i, line in enumerate(f_obj, 1):
#         print(f'Line {i}: {len(line.split())} word(s)')


"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""
# with open('dz_5_3.txt', 'r', encoding='utf-8') as f_obj:
#     salary_all = []  # salary list of all employees
#     salary_less20 = []  # salary list of employees with salary < 20000
#
#     print("Employees with salary < 20000 rub:")
#     for line in f_obj:
#         employee_info = line.split()
#         salary_all.append(float(employee_info[1]))
#         if float(employee_info[1]) < 20000:
#             salary_less20.append(float(employee_info[1]))
#             print(employee_info[0])
#
# print(f'\nAverage salary (salary < 20000 rub): {(sum(salary_less20) / len(salary_less20)):.2f} rub')
# print(f'Average salary (all): {(sum(salary_all) / len(salary_all)):.2f} rub')


"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""
# accordance_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре",}
# info_list = []
#
# with open("dz_5_4.txt", "r", encoding="utf-8") as f_obj:
#     with open("dz_5_4_rus.txt", "w", encoding="utf-8") as wf_obj:
#         for line in f_obj:
#             info_list = line.split()
#             info_list[0] = accordance_dict[info_list[0]]
#             print(" ".join(info_list), file=wf_obj)


"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""
# with open('dz_5_5.txt', 'w', encoding='utf-8') as f_obj:
#     f_obj.write(str(' '.join([str(i) for i in range(20) if i % 2 == 0])))
#
# with open('dz_5_5.txt', 'r', encoding='utf-8') as f_obj:
#     line = f_obj.read().split()
#     print(f"Numbers in file:\n{line}\n")
#     print(f"Sum of numbers in file: {sum(list(map(int, line)))}")


"""6. Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран. {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""
# subject_dict = {}
# with open('dz_5_6.txt', 'r', encoding='utf-8') as f_obj:
#     for subj_line in f_obj:
#         subj_list = subj_line.split()
#         hours_sum = 0
#         for lesson_type_index in range(1, len(subj_list)):  # бежим по элементам: 100(л) 50(пр) 20(лаб)
#             lesson_type_hours = "0"
#             for i in subj_list[lesson_type_index]:  # бежим по элементу: пример 100(л), выцепляем число
#                 if i.isdigit():
#                     lesson_type_hours += i  # конкатинируем часы одного типа занятий: пример 0+1+0+0
#             hours_sum += int(lesson_type_hours)
#         subject_dict[subj_list[0][:-1]] = hours_sum  # формируем элемент словаря: например {'Информатика': 170}
# print(subject_dict)


"""7.Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
"""
import json

firms_profit = {}
average_profit = []  # для накопления прибылей фирм без убытков
answer_list = []
with open('dz_5_7.txt', 'r', encoding='utf-8') as f_obj:
    for subj_line in f_obj:
        firm_data_list = subj_line.split()
        profit = int(firm_data_list[2]) - int(firm_data_list[3])
        firms_profit[firm_data_list[0]] = abs(profit)  # заполняем словарь {фирма: прибыль/убыток}
        if profit > 0:
            average_profit.append(profit)

answer_list.append(firms_profit)
answer_list.append({'average_profit': int(sum(average_profit) / len(average_profit))})

with open("dz_5_7.json", "w") as write_f:
    json.dump(answer_list, write_f)
