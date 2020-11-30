"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""

import json

def profits(filename):
    result = dict()
    with open(filename, 'r') as file:
        for line in file:
            split = line.split(" ")
            result[split[0]] = int(split[2]) - int(split[3])
    return result


def average_profit(profits):
    positives = list(x for x in profits.values() if x > 0)
    return int(sum(positives) / len(positives))


def save_into_json(profits, average_profit):
    with open('firms_report.json', 'w') as file:
        json.dump([profits, {'average_profit': average_profit}], file)


profits = profits('firms.txt')
average_profit = average_profit(profits)
save_into_json(profits, average_profit)
