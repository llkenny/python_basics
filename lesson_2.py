# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе. 
def exercise_1():
    list = ["13", "test", "True", True, 13, 14.1, None, {1, 2, 3}, [1, 2, 3], (1, 2, 3), {'key': 'value'}]

    for element in list:
        print(f'{element} is {type(element)}')

# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
def exercise_2():
    values_list = list()

    while True:
        try:
            values_list.append(input(f'Add value ({exit}): '))
        except EOFError:
            break
            
    print(f'\n1List: {values_list}')
    count = len(values_list)

    if count > 1:
        i = 1
        while i < count:
            values_list[i], values_list[i-1] = values_list[i-1], values_list[i]
            i += 2
            
    print(f'Swap: {values_list}')

# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
def exercise_3():
    seasons_list = [          "winter", "winter",
                    "spring", "spring", "spring",
                    "summer", "summer", "summer",
                    "autumn", "autumn", "autumn",
                    "winter"]

    seasons_dict = {12: "winter", 1: "winter", 2: "winter",
                    3: "spring", 4: "spring", 5: "spring",
                    6: "summer", 7: "summer", 8: "summer",
                    9: "autumn", 10: "autumn", 11: "autumn"}

    number = int(input("Enter month number: "))
    print(seasons_list[number-1])
    print(seasons_dict[number])

exercise_1()
exercise_2()
exercise_3()