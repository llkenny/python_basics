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

exercise_1()
exercise_2()