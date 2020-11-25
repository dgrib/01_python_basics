"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""
with open('dz_5_2.txt', 'r', encoding='utf-8') as f_obj:
    for i, line in enumerate(f_obj, 1):
        print(f'Line {i}: {len(line.split())} word(s)')
