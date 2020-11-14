# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user(**kwargs):
    return f'Name: {kwargs["name"]}, Surname: {kwargs["surname"]}, Date of Birth: {kwargs["dob"]}, City: {kwargs["city"]}, Email: {kwargs["email"]}, Phone: {kwargs["phone"]}'

kwargs = {"name": "", "surname": "", "dob": "", "city": "", "email": "", "phone": ""}
for key in kwargs.keys():
    value = input(f'Enter {key}: ')
    kwargs[key] = value

print(user(**kwargs))
