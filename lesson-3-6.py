"""6 Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text
"""


def int_func(word):
    """Does the first letter capitalized: 'text' into 'Text'."""
    # return word.capitalize()
    return chr(ord(word[0]) - 32) + word[1:]


string = input('Enter divided spaces words of lower case letters, symbols or numbers: ')
string_list = string.split(' ')
clean_string_list = []
for i in string_list:  # checking if other symbols than a-z A-Z are in entered string
    counter = 0
    for j in i:
        if 0 <= ord(j) <= 64 or 91 <= ord(j) <= 96 or 123 <= ord(j):
            counter += 1
    if counter == 0:
        clean_string_list.append(i.lower())

clean_string_list = list(map(int_func, clean_string_list))
print(f'Your entered string: \n{string}')
new_string = ' '.join(clean_string_list)
print(f'Cleaned capitalized string: \n{new_string}')
