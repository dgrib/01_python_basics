"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""
accordance_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре",}
info_list = []

with open("dz_5_4.txt", "r", encoding="utf-8") as f_obj:
    with open("dz_5_4_rus.txt", "w", encoding="utf-8") as wf_obj:
        for line in f_obj:
            info_list = line.split()
            info_list[0] = accordance_dict[info_list[0]]
            print(" ".join(info_list), file=wf_obj)
