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
