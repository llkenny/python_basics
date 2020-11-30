# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

from functools import reduce

with open('salary.txt', 'r') as file:
    salary = list(map(lambda x: x.rstrip().split(" "), file.readlines()))

    print(f'< 20000: {list(s[0] for s in salary if float(s[1]) < 20000)}')
    print(f'Mean: {sum(float(x[1]) for x in salary) / len(salary)}')
