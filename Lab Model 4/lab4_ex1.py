user_name = input('Введите имя: ')
user_age = int(input('Введите ваш возраст: '))
user_home = input('Введите ваш город проживания: ')


def create_user_info(name, age, city):
    str_user = f'Ваше имя {name}, ворзраст {age}, город прожиания {city}'
    return str_user

print(create_user_info(user_name, user_age, user_home))