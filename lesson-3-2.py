"""2 Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def print_user_data(name, sn, birth, city, email, phone):
    """Prints user's data"""
    print(f'\nName: {name}; Surname: {sn}; Birth date: {birth}; City: {city}; Email: {email}; Phone number: {phone}')


print_user_data(
    name=input("Enter user's name: ").capitalize(),
    sn=input("Enter user's surname: ").capitalize(),
    birth=input("Enter user's birth date: "),
    city=input("Enter user's city: ").capitalize(),
    email=input("Enter user's email: "),
    phone=input("Enter user's phone number: "),
    )
