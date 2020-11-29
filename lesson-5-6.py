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


subject_dict = {}
with open('dz_5_6.txt', 'r', encoding='utf-8') as f_obj:
    for s in f_obj:
        subject_dict[s.split(':')[0]] = sum(map(int, ''.join((i if i.isdigit() else ' ') for i in s).split()))
    print(subject_dict)
