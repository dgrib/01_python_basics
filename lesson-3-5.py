"""5 Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
"""


def sum_func():
    """Adds user's numbers to a sum"""
    sum_all = 0
    quit_check = True

    while quit_check:
        user_data = input('Enter spaces divided data for sum counting (q for quit): ')
        user_data_list = user_data.split()

        if 'q' in user_data_list:
            user_data_list.remove('q')
            quit_check = False
        for i in range(len(user_data_list)):  # cleaning list from strings like ['ewf' 34 2 'et']
            try:
                int(user_data_list[i])
            except ValueError:
                user_data_list[i] = 0

        sum_iter = sum(map(int, user_data_list))
        sum_all += sum_iter
        print(f'Last iteration sum: {sum_iter}, All elements sum: {sum_all}')


sum_func()
