"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""
# with open('dz_5_5.txt', 'w', encoding='utf-8') as f_obj:
#     f_obj.write(str(' '.join([str(i) for i in range(20) if i % 2 == 0])))
#
# with open('dz_5_5.txt', 'r', encoding='utf-8') as f_obj:
#     line = f_obj.read().split()
#     print(f"Numbers in file:\n{line}\n")
#     print(f"Sum of numbers in file: {sum(map(int, line))}")


with open('dz_5_5.txt', 'w+', encoding='utf-8') as f_obj:
    f_obj.write(str(' '.join([str(i) for i in range(20) if i % 2 == 0])))
    # поднимаем курсор вверх
    f_obj.seek(0)
    line = f_obj.readline().split()
    print(f"Numbers in file:\n{line}\n")
    print(f"Sum of numbers in file: {sum(map(int, line))}")
