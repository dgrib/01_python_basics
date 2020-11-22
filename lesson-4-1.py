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
