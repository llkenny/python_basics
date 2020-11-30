"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:

Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:

{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

def string_to_ints(s):
    result = list()
    number = ""
    for c in s:
        if c.isdigit():
            number += c
        elif len(number) > 0:
            result.append(int(number))
            number = ""
    return result


def calc_hours(filename):
    result = dict()
    with open(filename, 'r') as file:
        for line in file:
            split = line.split(":")
            result[split[0]] = sum(string_to_ints(split[1]))
    return result


print(calc_hours("lessons.txt"))
