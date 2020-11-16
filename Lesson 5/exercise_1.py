# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('1.txt', 'w') as file:
    while True:
        new_line = input("Enter new line: ")
        if len(new_line) == 0:
            break
        file.write(f'{new_line}\n')
