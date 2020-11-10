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
            
    print(f'\nList: {values_list}')
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

# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
def exercise_4():
    string = input("Enter string: ")
    words = string.split(" ")
    i = 0
    while i < len(words):
        print(f'{i}: {words[i][:10]}')
        i += 1

# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
def exercise_5():
    my_list = [7, 5, 3, 3, 2]
    print(my_list)
    new_value = int(input("Enter new value (int): "))
    i = 0
    while i < len(my_list) and my_list[i] >= new_value:
        i += 1
    my_list.insert(i, new_value)

    print(f'Index to insert: {i}\nNew list: {my_list}')

# * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
def exercise_6():
    items = list()
    index = 1

    while True:
        try:
            title = input(f"Enter item name {exit}: ")
            price = int(input(f"Enter price (int) {exit}: "))
            quantity = int(input(f"Enter quantity (int) {exit}: "))
            unit = input(f"Enter unit {exit}: ")
        except EOFError:
            print()
            break
        item = (index, {"название": title, "цена": price, "количество": quantity, "eд": unit})
        items.append(item)
        index += 1
    
    print(items)
    names = set()
    prices = set()
    quantities = set()
    units = set()

    for item in items:
        names.add(item[1]["название"])
        prices.add(item[1]["цена"])
        quantities.add(item[1]["количество"])
        units.add(item[1]["eд"])

    result = {"название": list(names), "цена": list(prices), "количество": list(quantities), "eд": list(units)}
    print(result)

exercise_1()
exercise_2()
exercise_3()
exercise_4()
exercise_5()
exercise_6()