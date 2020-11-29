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


with open('dz_5_3.txt', 'r', encoding='utf-8') as f_obj:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in f_obj}
    print(f"Employees with salary < 20k: {', '.join([item[0] for item in employees_dict.items() if item[1] < 20000])}")
    print(f"All employees average salary: {(sum(employees_dict.values()) / len(employees_dict)):.2f}")
